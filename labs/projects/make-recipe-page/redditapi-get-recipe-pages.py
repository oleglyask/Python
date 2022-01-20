# Using the external `praw` package, fetch recipes through the Reddit API
import praw
import os
from pprint import pprint
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

reddit = praw.Reddit(
    client_id=os.environ.get('reddit_client_id'),
    client_secret=os.environ.get('reddit_client_secret'),
    user_agent="pc:python_class_codingnomads:v1 (by u/oleglyask)",
)


subreddit = reddit.subreddit('recipes')
print(subreddit.description)