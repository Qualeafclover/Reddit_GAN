from configs import *
import praw
import praw.models
import os
import shutil
import datetime

class Logger(object):
    def __init__(self, logdir=LOGGER_DIRECTORY, verbose=LOGGER_VERBOSE):
        if not os.path.isdir(logdir):
            os.mkdir(logdir)
        now = datetime.datetime.now()
        log_filename = now.strftime('|%Y_%m_%d|%H_%M_%S|.txt')
        self.verbose = verbose
        self.log_path = os.path.join(logdir, log_filename)
        self.log_start_time()

    def time_log(self, log_content:str, logtype='I'):
        now = datetime.datetime.now()
        now = now.strftime('|%Y_%m_%d|%H_%M_%S|')
        with open(self.log_path, 'a') as f:
            f.write("{} ({}) {}\n".format(now, logtype, log_content))
        print("{} ({}) {}".format(now, logtype, log_content))
        return now

    def log_start_time(self):
        self.time_log('Started program instance.')

    def log_reddit_login(self):
        self.time_log('Successfully started bot instance.')

    def log_loaded_model(self):
        self.time_log('Successfully loaded model in.')

    def log_mention(self, mention:praw.models.Comment):
        self.time_log(f'Recieved mention by u/{mention.author}.')
        self.time_log(f'Comment id: {mention.id}')
        self.time_log(f'Comment body: {mention.body}')

    def log_args(self, args):
        self.time_log('Recieved arguments for generator:')
        self.time_log(args)

    def log_bad_args(self):
        self.time_log('Unable to understand arguments provided. Replying with an error message.', logtype='W')

    def log_replied(self):
        self.time_log('Reply successful.')

    def log_image_post(self, submission:praw.models.Submission):
        self.time_log('Successfully submitted image.')
        self.time_log(f'Submission id: {submission.id}')
        self.time_log(f'Image url: {submission.url}')

    def log_image_gen(self):
        self.time_log('Successfully generated image.')

def test():
    logger = Logger()
    logger.log_reddit_login()

if __name__ == '__main__':
    test()