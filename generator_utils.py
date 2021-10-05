from configs import *
import numpy as np
import torch
import cv2

def get_args(reddit_call:str):
    reddit_call = reddit_call.lower()
    reddit_call = reddit_call.replace('\\', '')
    bot_name = f'u/{REDDIT_USERNAME}'.lower()

    args = {'seed': None, 'trunc':GENERATOR_TRUNC}

    reddit_call = reddit_call.split()
    if reddit_call[0] != bot_name: return None

    for reddit_call_ in reddit_call[1:]:
        if not reddit_call_.startswith('--'): return None
        reddit_call_ = reddit_call_[2:].split('=')
        if len(reddit_call_) != 2: return None
        if reddit_call_[0] not in args: return None
        try:
            if reddit_call_[0].lower() == 'seed':
                arg_in = int(reddit_call_[1])
            if reddit_call_[0].lower() == 'trunc':
                arg_in = float(reddit_call_[1])
        except ValueError: return None
        args[reddit_call_[0]] = arg_in
    return args

def generate(G, device:torch.device, seed:int, trunc:float) -> np.ndarray:
    z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)

    w = G.mapping(z, None, truncation_psi=trunc)
    img = G.synthesis(w, noise_mode='const')

    img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
    img = img.cpu().numpy()[0]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

if __name__ == '__main__':
    args = get_args('u/Nitori-bot --trunc=0.5')
    print(args)
