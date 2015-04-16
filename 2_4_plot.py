k = open('retweet_count', 'r')
count = [0 for i in range(1194)]
i=0
for line in k.readlines():
	count[i]=int(line)
	i+=1

k.close()

###########plot k tweets retweeted k times graph
import numpy as np
import matplotlib.pyplot as plt

k=np.arange(1,1195,1)
plt.plot(k[0:100],count[0:100])
plt.xlabel('retweeted times')
plt.ylabel('number of tweets')
plt.title('number of tweets versus retweeted k times')
plt.show()


klog = np.log(k[0:100])
countlog = np.log(count[0:100])
p1=plt.plot(klog,countlog)
plt.xlabel('log of retweeted times')
plt.ylabel('log of number of tweets')
plt.title('log-log: number of tweets versus retweeted k times')
x=[0,2]
y=[12.7,0]
p2=plt.plot(x,y,'r')
plt.show()
