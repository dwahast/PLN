import tweepy
import os
import tweepy as tw
import pandas as pd
import re

df = pd.read_csv('dataset.ptbr_tweets.txt', sep="\t")

#get this tokens and keys on Twitter Developer
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def createSet(corpus):

    DataSet = []
    for index, tweet in corpus.iterrows():

        try:
            tweetFetched = api.get_status(tweet["tweet_id"])
            print("Tweet fetched:\n" + tweetFetched.text)
            DataSet.append((tweet["tweet_id"],tweetFetched.text))

        except:
            print("Exception")
            continue

    return DataSet

resultFile = createSet(df.drop_duplicates(subset= ['tweet_id']).head(10))
