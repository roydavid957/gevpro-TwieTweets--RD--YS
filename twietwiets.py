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
		self.prondict = {}
		for line in self.pronfile:
			pronlist.append(line.split("\\"))
		for pron_word in pronlist:
			key = pron_word[1]
			value = pron_word[3]
			self.prondict[key] = value
		return self.prondict
		
	def get_usable_tweets(self):
		tweetlist = []
		last_word = []
		self.usable_tweetlist = []
		for line in self.tweetfile:
			tweetlist.append(line.split())
		for tweet in tweetlist:
			last_word.append(tweet[-1])
		for word in last_word:
			if word in self.prondict:
				self.usable_tweetlist.append(tweet)#gaat niet door naar volgende tweet
		print(self.usable_tweetlist)#print aldoor dezelfde tweet
		"""for line in self.tweetfile:
			tweetlist.append(line.split())
			for tweet in tweetlist:
				last_word.append(tweet[-1])
				for word in last_word:
					if word in self.prondict:
						self.usable_tweetlist.append(tweet)#gaat niet door naar volgende tweet
		print(self.usable_tweetlist)#print aldoor dezelfde tweet"""#dit ook al geprobeerd, programma blijft dan hangen, print niets

				
if __name__ == "__main__":
	twietwiets()
