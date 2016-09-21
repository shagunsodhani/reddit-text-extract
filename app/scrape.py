from time import sleep
from time import time

import praw

from config import parse_config
from readability import parse_url

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


def scrape_reddit_text():
    file_to_save_to = config['path_to_save']
    start_time = time()
    counter = 0
    with open(file_to_save_to, 'w') as f:
        reddit = praw.Reddit(user_agent=config['user_agent'])
        for subreddit, limit in read_subreddit_list():
            text = ''
            for submission in reddit.get_subreddit(subreddit).get_hot(limit=limit):
                sleep(1)
                counter += 1
                if (counter % 1000 == 0):
                    end_time = time()
                    print(str(counter) + " number of submissions parsed in "
                          + str(end_time - start_time) + " seconds.")
                    start_time = end_time
                if (submission.selftext):
                    text = submission.title.strip() + "\n" + \
                           submission.selftext.strip()
                else:
                    text = parse_url(submission.url).strip()
                for comment in submission.comments:
                    text += "\n" + comment.body.strip()
                text = ' '.join(text.split()).strip()
                if (text):
                    f.write(text.strip() + "\n")
                    print(text.strip())


if __name__ == "__main__":
    scrape_reddit_text()
