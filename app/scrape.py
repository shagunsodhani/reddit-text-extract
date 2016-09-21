import praw

from config import parse_config

config = parse_config("local")

def read_subreddit_list():
    subreddit_list_path = config['subreddit_list_path']
    subreddit_limit_list = []
    with open(subreddit_list_path) as f:
        for _line in f:
            line = _line.strip().split()
            subreddit = line[0]
            if (len(line) > 1 and line[1]):
                limit = line[1]
            else:
                limit = None
            subreddit_limit_list.append((subreddit, limit))
    return subreddit_limit_list


reddit = praw.Reddit(user_agent=config['user_agent'])

for subreddit, limit in read_subreddit_list():
    for submission in reddit.get_subreddit(subreddit).get_hot(limit=limit):
        if (submission.selftext):
            text = submission.title + "\n" + submission.selftext
            print(text)
        else:
            text = submission.url
            print("url")
        for comment in submission.comments:
            text += "\n" + comment.body
        print(text)
