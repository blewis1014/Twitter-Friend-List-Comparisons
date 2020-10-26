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

# STREAM_CAP = 5
STREAM_CAP = User.friends_count
friend_list=[] # {'USER': ID, 'FRIENDCOUNT': count}
sortedFriends=[]

def process():
    try: 
        for follower in tweepy.Cursor(api.friends, user_ID).items(STREAM_CAP):
            friend_ID = follower.screen_name
            print("Processing "+friend_ID+"...")
            friend_count = follower.friends_count
            friend_dict = {'USER': friend_ID, 'FRIENDCOUNT': friend_count}
            friend_list.append(friend_dict)
            print("Finshed"+'\n')
    except tweepy.RateLimitError:
        print ("Rate Limit reached. Sleeping for 60s")
        time.sleep(60)

    friend_list.append({'USER': user_ID, 'FRIENDCOUNT': STREAM_CAP})

    global sortedFriends
    sortedFriends = sorted(friend_list, key=itemgetter('FRIENDCOUNT'))


def getFollowerCount(userName):
    c = tweepy.Cursor(api.followers, userName)

    count = 0
    for follower in c.items(): 
        count += 1

    return count

def writeOutput():
    for item in sortedFriends:
        print(str(item))

def writeToFile():
    with open("FriendsList.txt","w") as f:
        for item in sortedFriends:
            f.write(str(item)+'\n')

if __name__=='__main__':
    process()
    writeOutput()
    writeToFile()

