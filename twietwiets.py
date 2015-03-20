#!usr/bin/python3
#twietwiets.py
#Roy David & Youri Schuur

import sys
from PyQt4 import QtGui, QtCore 
import random

class twietwiets():
	def __init__(self):
		super(twietwiets, self).__init__()
		self.tweetfile = open("tweets.txt", "r")
		self.pronfile = open("dpw.cd", "r")
		self.create_prondict()
		self.get_usable_tweets()
		
	def create_prondict(self):
		pronlist = []
		prondict = {}
		for line in self.pronfile:
			pronlist.append(line.split("\\"))
		for pron_word in pronlist:
			key = pron_word[1]
			value = pron_word[3]
			prondict[key] = value
		return prondict
		
	def get_usable_tweets(self):
		tweetlist = []
		last_word = []
		usable_tweetlist = []
		for line in self.tweetfile:
			tweetlist.append(line.split())
		for tweet in tweetlist:
			last_word.append(tweet[-1])
		for word in last_word:
			if word in self.create_prondict():#dit werkt niet, hij slaat dit over of
				usable_tweetlist.append(tweet)#krijgt niets terug, print lege lijst
		print(usable_tweetlist)

				
if __name__ == "__main__":
	twietwiets()
