
f = open('search_log.txt','r')
k = open('3_per5sec','w')
g = open('5_per5sec','w')
# k is for the most popular hashtag, and g is for the second one. 
# k combined with g are useful in part 5.

knum = []
gnum = []

count = 0
num = [0,0,0,0,0]
for line in f.readlines():
	#based on observation, the 1st and 2nd hashtap are the most and second most popular ones
	#they have count number 1~3600 and 3601~7200 respectively
	group = count/3600
	tmp = line[line.rindex('No. Of Results: ')+16 : len(line)-1]
	num[group] += int(tmp)
	count += 1
	if group == 0:
		k.write(tmp)
		k.write('\n')
		knum.append(int(tmp))
	if group == 1:
		g.write(tmp)
		g.write('\n')
		gnum.append(int(tmp))

for n in num:
	print n

f.close()
k.close()
g.close()

#######plot bar graph of total number of each hashtag
import matplotlib.pyplot as plt
import numpy as np
N=5
hashtags = ['SB49', 'football', 'MakeSafeHappen', 'brandbowl', 'adbowl']
ind = np.arange(N)
ax = plt.subplot()
width=0.35
rects = ax.bar(ind+width,num,width)
ax.set_xticks(ind+width*1.5)
ax.set_xticklabels(hashtags)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects)

plt.xlabel('HashTag')
plt.ylabel('Number of Tweets')
plt.title('Total Number of Tweets')
plt.show()


########plot number of tweets per second
x=np.arange(0,18000,5)
ratio = np.true_divide(gnum,knum)
plt.plot(x,knum)
plt.xlabel('timeserial')
plt.ylabel('number of tweets')
plt.title('number of tweets for #SB49 per second')
plt.show()
plt.plot(x,ratio)
plt.xlabel('timeserial')
plt.ylabel('ratio of second over first popular tweets')
plt.title('correlation between first and second popular hashtags')
plt.show()











