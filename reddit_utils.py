from configs import *
import praw
import praw.models

def setup_reddit() -> praw.Reddit:
    reddit = praw.Reddit(
        client_id=REDDIT_ID,
        client_secret=REDDIT_SECRET,
        user_agent=f'User-Agent:{REDDIT_ID}:{REDDIT_PROGRAM_VERSION} (by /u/{REDDIT_CREATOR})',
        password=REDDIT_PASSWORD, username=REDDIT_USERNAME
    )
    reddit.validate_on_submit = True
    return reddit

def submit_image(reddit:praw.Reddit, *args, **kwargs) -> praw.models.Submission:
    subreddit = reddit.subreddit(f'u_{REDDIT_USERNAME}')
    submission = subreddit.submit_image(*args, **kwargs)
    return submission