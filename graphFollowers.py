import csv 
import matplotlib 
import matplotlib.pyplot as plt
import statistics
import math
import pandas as pd 
from operator import itemgetter
import ast

followers=[]  # {'USER': 'name', 'FRIENDCOUNT': 'count'}
User = 'weiglemc'
mean = 1
standard = 1
median = 1

def process():
    with open("FollowerList.txt",'r') as f:
        count = 1
        for line in f:
            new_dict = ast.literal_eval(line)
            followers.append(new_dict)
            count+=1
        
        global mean,standard,median
        mean = calcMean()
        standard = calcStandDevi()
        median = calcMedian()

def calcMean():
    friend_counts = []
    for user in followers:
        friend_counts.append(int(user['FOLLOWERCOUNT']))
    
    result = statistics.mean(friend_counts)

    return math.trunc(result)

def calcStandDevi():
    friend_counts = []
    for user in followers:
        friend_counts.append(int(user['FOLLOWERCOUNT']))
    
    result = statistics.pstdev(friend_counts)
    return round(result,2)

def calcMedian():
    friend_counts = []
    for user in followers:
        friend_counts.append(int(user['FOLLOWERCOUNT']))
    
    friend_counts.sort()
    mid = statistics.median(friend_counts)

    return math.trunc(mid)

def drawGraph():
    x=[]
    y=[]
    ux=[]
    uy=[]
    for per in followers:
        x.append(per['USER'])
        y.append(per['FOLLOWERCOUNT'])
        if(per['USER']==User):
            ux.append(per['USER'])
            uy.append(per['FOLLOWERCOUNT'])

    plt.title('Friendship Paradox: User "'+User+'"')
    plt.xlabel(User+' vs. their followers')
    plt.ylabel('# of followers')

    plt.scatter(x,y, label=User+"'s followers")
    plt.tick_params(axis='x', which='both',bottom=False, labelbottom=False)   
    plt.scatter(ux,uy,color='yellow', label=User)
    plt.legend(loc="upper left")
    
    plt.show()

    

    
    

def writeResults():
    print("Statistics for 'Follower' counts of "+User+" and their followers")
    print("Mean: "+str(mean))
    print("Median: "+str(median))
    print("Standard Deviation: "+str(standard))

    with open("FollowerStatisticsTrimmed.txt","w") as f:
        f.write("Statistics for 'Follower' counts of "+User+" and their followers"+'\n')
        f.write("Mean: "+str(mean)+'\n')
        f.write("Median: "+str(median)+'\n')
        f.write("Standard Deviation: "+str(standard))

if __name__ == '__main__':
    process()
    writeResults()
    drawGraph()
