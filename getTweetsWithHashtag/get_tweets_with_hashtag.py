"""
Simply Python3 script for Stackoverflow question
- http://stackoverflow.com/questions/41684729/anyway-to-increase-twitter-mining-speed/41707536#41707536
Get old tweets with a specific hashtag and write them in a json file
"""
from getTweetsWithHashtag.getOldTweets import got3
import json

data = {}
tweetCriteria = got3.manager.TweetCriteria().setQuerySearch('#happy').setSince("2016-05-01")
tweets = got3.manager.TweetManager.getTweets(tweetCriteria)

for idx, tweet in enumerate(tweets):
    data[idx] = tweet.text

with open('tweets_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
