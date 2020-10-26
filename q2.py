import matplotlib 
import matplotlib.pyplot as plt
import statistics
import math
import pandas as pd 
from operator import itemgetter
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

# Keys ommitted 
consumer_key="***"
consumer_secret="***"
access_token="***"
access_secret="***"

# Handles authorization with Twitter
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# api = tweepy.API(auth)

user_ID = 'weiglemc'
User=api.get_user(user_ID)

# STREAM_CAP = 433
STREAM_CAP = User.followers_count
followers=[] # {'USER': ID, 'FOLLOWERCOUNT': count}
sortedFollowers=[]

def process():
    try: 
        for follower in tweepy.Cursor(api.followers, user_ID).items(STREAM_CAP):
            follower_ID = follower.screen_name
            print("Processing "+follower_ID+"...")
            follower_count = follower.followers_count
            follower_dict = {'USER': follower_ID, 'FOLLOWERCOUNT': follower_count}
            followers.append(follower_dict)
            print("Finshed"+'\n')
    except tweepy.RateLimitError:
        print ("Rate Limit reached. Sleeping for 60s")
        time.sleep(60)

    followers.append({'USER': user_ID, 'FOLLOWERCOUNT': User.followers_count})

    global sortedFollowers
    sortedFollowers = sorted(followers, key=itemgetter('FOLLOWERCOUNT'))


def getFollowerCount(userName):
    c = tweepy.Cursor(api.followers, userName)

    count = 0
    for follower in c.items(): 
        count += 1

    return count

def writeOutput():
    for item in followers:
        print(str(item))

def writeToFile():
    with open("FollowerList.txt","w") as f:
        for item in sortedFollowers:
            f.write(str(item)+'\n')

if __name__=='__main__':
    process()
    writeOutput()
    writeToFile()

