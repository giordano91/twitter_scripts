#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
A Python 3.X script to get the most popular two hashtags from specific user.
Return a list.

"""
import tweepy
from tweepy import OAuthHandler, StreamListener


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    hashtags_dict = {}

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='GiordanoS91', count=200)

    for tweet in tweets:
        hashtags = tweet.entities.get('hashtags')
        for hashtag in hashtags:
            if hashtag['text'] in hashtags_dict.keys():
                hashtags_dict[hashtag['text']] += 1
            else:
                hashtags_dict[hashtag['text']] = 1

    print(sorted(hashtags_dict, key=hashtags_dict.get, reverse=True)[:2])
