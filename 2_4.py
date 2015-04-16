import json

# We have found out the maximum retweet_count is 1193
'''
f = open('tweets.txt', 'r')
max_retw = -1
count = 0
for line in f.readlines():
	tmp = json.loads(line)
	retw = tmp['tweet']['retweet_count']
	if retw > max_retw:
		max_retw = retw
	count += 1
print max_retw
print count
f.close()
'''

f = open('tweets.txt', 'r')
k = open('retweet_count.txt', 'w')
count = [0 for i in range(1200)]

for line in f.readlines():
	tmp = json.loads(line)
	retw = tmp['tweet']['retweet_count']
	if int(retw) < 0:
		print 'Number of retweets should be nonnegative !'
		break
	count[int(retw)] += 1
	
total = 0
for i in range(1194):
	k.write(str(count[i]))
	k.write('\n')
	total += count[i]
	
print total
f.close()
k.close()












