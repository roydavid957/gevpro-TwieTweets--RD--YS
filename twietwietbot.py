#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, twietwiets

CONSUMER_KEY = 'NkO6DvRBtf6LMg4uKS5ip8ly0'
CONSUMER_SECRET = 'ER9uOTsYkkjF7AntiFGJQn9GrowaR133F2Uik1h4xMTv23Y7Ll'
ACCESS_KEY = '3115005287-qmh9xd4wXXqftCxyf1BHW7oRvQHcUKDwTmU6BCo'
ACCESS_SECRET = 'JSn387CHzXcN99iBvXbADGvR51pTQpmYD2w2Rvz9gDydZ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

"""Van het groepje: TweetMe overgenomen"""
twieTweet = twietwiets.twietwiets()
while 1 > 0:
    twietwiet = twieTweet.get_twietwiet()
    print(twietwiet)
    line1 = " ".join(twietwiet[0])
    line2 = " ".join(twietwiet[1])
    tweet = line1 + '\n' + line2
    if len(line1) <= 128 and len(line2) <= 128:
        api.update_status(status=tweet)
        time.sleep(3600)

"""used this tutorial: http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/"""
