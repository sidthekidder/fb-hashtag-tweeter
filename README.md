# fb-hashtag-tweeter
A simple tweet bot that scrapes hashtagged posts from the public facebook API. 

- `pip install selenium twitter`
- create a new twitter app on [https://www.apps.twitter.com](https://www.apps.twitter.com) and generate its API keys
- fill in your twitter API keys in `config.py`
- fill in the hashtag you want to scrape
- run `python scripts.py`

This uses a simple text file as a log for previously scraped posts. You can schedule the `python scripts.py` to run regularly using cron or Windows Task Scheduler or what-have-you.
