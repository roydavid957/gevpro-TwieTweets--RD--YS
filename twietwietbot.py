#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aanroep:
installeer pip en tweepy.
kopieer de mappen pip, tweepy en six.1.9... en het bestand six.py
naar dezelfde map waar twietwietbot ook in zit.
roep aan met ./twietwietbot.py
"""

import tweepy, time, sys, twietwiets
import twitter_cfg as cfg

auth = tweepy.OAuthHandler(cfg.CONSUMER_KEY, cfg.CONSUMER_SECRET)
auth.set_access_token(cfg.ACCESS_KEY, cfg.ACCESS_SECRET)
api = tweepy.API(auth)

"""Van het groepje: TweetMe overgenomen"""
twieTweet = twietwiets.twietwiets()
while 1 > 0:
    twietwiet = twieTweet.get_twietwiet()
    """print kun je behouden als je wilt zien
    wat er getweet wordt zonder op twitter te kijken"""
    line1 = " ".join(twietwiet[0])
    line2 = " ".join(twietwiet[1])
    tweet = line1 + '\n' + line2
    print(tweet)
    if len(tweet) <= 140:
        api.update_status(status=tweet)
        """tijd is in seconden, verander simpelweg door 3600 te veranderen naar de tijd
        die je liever hebt"""
        time.sleep(3600)
    else:
        twietwiet = twieTweet.get_twietwiet()
        line1 = " ".join(twietwiet[0])
        line2 = " ".join(twietwiet[1])
        tweet = line1 + '\n' + line2
        print(tweet) 

"""used this tutorial: http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/"""
