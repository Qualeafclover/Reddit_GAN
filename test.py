import pickle
import torch
import numpy as np
import cv2

device = torch.device('cuda')

with open('model.pkl', 'rb') as f:
    G = pickle.load(f)['G_ema'].cuda()

POINTS = 50
INTERPOLATE = 100
TRUNC = 0.3
seed = None

z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)
from_w = G.mapping(z, None, truncation_psi=TRUNC)

for _ in range(POINTS):
    z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)
    to_w = G.mapping(z, None, truncation_psi=TRUNC)

    for balance in range(INTERPOLATE):
        balance = balance/INTERPOLATE

        w = from_w * (1 - balance) + \
            to_w * balance

        # print(w.shape)
        img = G.synthesis(w, noise_mode='const')

        img = (img.permute(0, 2, 3, 1) * 127.5 + 128).clamp(0, 255).to(torch.uint8)
        img = img.cpu().numpy()[0]

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # cv2.imwrite('test.png', img)
        cv2.imshow('', img)
        cv2.waitKey(1)

    from_w = to_w