# reddit-text-extract

Python code to extract all the text data from posts, urls and comments on various subreddits.

It is useful for collecting text corpus related to different domains when working on language modelling tasks.

## Usage

* `git clone git@github.com:shagunsodhani/reddit-text-extract.git`
* `sudo pip3 install requirements.txt`
* Add name of subreddits (to crawl data from) in `config/subreddit.txt`
* `cp config/config.cfg.sample config/config.cfg`
* Populate values in `config/config.cfg`
    * `user_agent` = user agent as defined by (praw)[https://praw.readthedocs.io/en/stable/] . Can put in any value.
    * `subreddit_list_path` = path to `config/subreddit.txt`
    * `path_to_save` = file path where crawled data is to be saved.
    * `readability_token` = token to use [Readability parser API](https://www.readability.com/developers/api/parser). Can be obtained from [here](https://www.readability.com/developers/api).
* `python3 scrape.py`
