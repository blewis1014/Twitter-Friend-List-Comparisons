import csv 
import matplotlib 
import matplotlib.pyplot as plt
import statistics
import math
import pandas as pd 
from operator import itemgetter

friends=[]  # {'USER': 'name', 'FRIENDCOUNT': 'count'}
sorted_friends=[]
User = 'U'
mean = 1
standard = 1
median = 1

def process():
    with open("HW4-friend-count.csv",'r') as f:
        count = 1
        for line in csv.DictReader(f):
            new_dict = {'USER':"f"+str(count),'FRIENDCOUNT':int(line['FRIENDCOUNT'])}
            friends.append(new_dict)
            count+=1
        
        friends.append({'USER':User, 'FRIENDCOUNT': len(friends)})

        global sorted_friends
        sorted_friends = sorted(friends, key=itemgetter('FRIENDCOUNT'))
      
        global mean,standard,median
        mean = calcMean()
        standard = calcStandDevi()
        median = calcMedian()

def calcMean():
    friend_counts = []
    for user in friends:
        friend_counts.append(int(user['FRIENDCOUNT']))
    
    result = statistics.mean(friend_counts)

    return math.trunc(result)

def calcStandDevi():
    friend_counts = []
    for user in friends:
        friend_counts.append(int(user['FRIENDCOUNT']))
    
    result = statistics.pstdev(friend_counts)
    return round(result,2)

def calcMedian():
    friend_counts = []
    for user in friends:
        friend_counts.append(int(user['FRIENDCOUNT']))
    
    friend_counts.sort()
    mid = statistics.median(friend_counts)

    return math.trunc(mid)

def drawGraph():
    x=[]
    y=[]
    ux=[]
    uy=[]
    for per in sorted_friends:
        x.append(per['USER'])
        y.append(per['FRIENDCOUNT'])
        if(per['USER']==User):
            ux.append(per['USER'])
            uy.append(per['FRIENDCOUNT'])

    plt.title('Friendship Paradox: User "'+User+'"')
    plt.xlabel(User+' vs. their friends')
    plt.ylabel('# of friends')

    plt.scatter(x,y, label=User+"'s friends")
    plt.tick_params(axis='x', which='both',bottom=False, labelbottom=False)   
    plt.scatter(ux,uy,color='yellow', label=User)
    plt.legend(loc="upper left")
    
    plt.show()

    

    
    

def writeResults():
    print("Statistics for 'Friend' counts of "+User+" and their friends")
    print("Mean: "+str(mean))
    print("Median: "+str(median))
    print("Standard Deviation: "+str(standard))

    with open("FriendStatistics.txt","w") as f:
        f.write("Statistics for 'Friend' counts of "+User+" and their friends"+'\n')
        f.write("Mean: "+str(mean)+'\n')
        f.write("Median: "+str(median)+'\n')
        f.write("Standard Deviation: "+str(standard))

if __name__ == '__main__':
    process()
    writeResults()
    drawGraph()
