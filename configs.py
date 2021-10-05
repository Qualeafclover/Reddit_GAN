##################
# LOGGER CONFIGS #
##################

LOGGER_DIRECTORY = 'logs'
LOGGER_VERBOSE = True

#####################
# GENERATOR CONFIGS #
#####################

GENERATOR_TRUNC = 0.7

##################
# REDDIT CONFIGS #
##################

REDDIT_PREFIX_COMMENT = \
'''
Thank you for using u/Nitori-bot!\n\n
'''

REDDIT_SUFFIX_COMMENT = \
'''
Kappa Kappa I am a bot.
'''

REDDIT_HELP_COMMENT = \
'''
I heard you call me, but I didn't understand what you wanted there...\n\n
For a simple drawing generation, type "u/Nitori-bot" (No quotation marks!)\n\n
For a custom drawing generation, type "u/Nitori-bot --seed={seed_number} --trunc={truncation value}" (No quotation marks!)\n\n
The number for seed must be 0 to 4294967295, and trunc must be from -128.0 to 127.0\n\n
Example for custom drawing generation:\n\n
u/Nitori-bot --seed=4649 --trunc=0.85\n\n
'''

REDDIT_PROGRAM_VERSION = 'v0.1.0'

REDDIT_MODEL = 'model.pkl'
REDDIT_TEMP_IMG = 'temp_gen.png'

# Fill in bot account details
REDDIT_USERNAME = 'Nitori-bot'
REDDIT_PASSWORD = ''
REDDIT_SECRET = ''
REDDIT_ID = ''

REDDIT_CREATOR = 'Qualeafclover'
REDDIT_SUBREDDIT = 'touhou'
REDDIT_LOGDIR = 'logs'

REDDIT_TEST_MODE = True
