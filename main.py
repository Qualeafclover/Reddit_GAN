from reddit_utils import *
from generator_utils import *
from configs import *
from logger import Logger
import praw.models
import praw
import time
import pickle
import torch
import numpy as np
import cv2

def main():
    # Setup logger
    logger = Logger()

    # Start generator
    device = torch.device('cuda')
    with open(REDDIT_MODEL, 'rb') as f:
        G = pickle.load(f)['G_ema'].cuda()
    logger.log_loaded_model()

    # Start reddit instance
    reddit = setup_reddit()
    logger.log_reddit_login()

    # Main loop
    while True:
        for item in reddit.inbox.unread(limit=50):
            if item in reddit.inbox.mentions(limit=None):
                logger.log_mention(mention=item)
                generator_args = get_args(item.body)
                if generator_args is not None:
                    if generator_args['seed'] is None:
                        generator_args['seed'] = np.random.randint(0, 4294967295)
                    if (0 > generator_args['seed']) or (generator_args['seed'] > 4294967295):
                        generator_args = None
                    elif (-128.0 > generator_args['trunc']) or (generator_args['trunc'] > 127.0):
                        generator_args = None

                if generator_args is None:
                    logger.log_bad_args()
                    item.reply(REDDIT_PREFIX_COMMENT+REDDIT_HELP_COMMENT+REDDIT_SUFFIX_COMMENT)
                    logger.log_replied()
                else:
                    logger.log_args(args=generator_args)
                    image = generate(G=G, device=device, seed=generator_args['seed'], trunc=generator_args['trunc'])
                    cv2.imwrite(REDDIT_TEMP_IMG, image)
                    logger.log_image_gen()
                    submission = submit_image(reddit=reddit, title=item.id, image_path=REDDIT_TEMP_IMG)
                    logger.log_image_post(submission=submission)
                    url = submission.url+'\n\n'
                    item.reply(REDDIT_PREFIX_COMMENT+url+REDDIT_SUFFIX_COMMENT)
                    logger.log_replied()
            item.mark_read()
        time.sleep(3)

if __name__ == '__main__':
    main()