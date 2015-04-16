import json
import sys
import datetime

# the input is the parameter in command line
# Example: python 2_6.py 250

num = int(sys.argv[1])
f = open('tweets.txt', 'r')
count = 0

for line in f.readlines():
	count += 1
	if count < num:
		continue
	tmp = json.loads(line)
	ts = int(tmp['firstpost_date'])
	print 'Post date: ' + str(datetime.datetime.fromtimestamp(ts))
	print 'Text: ' + tmp['tweet']['text']
	print 'Number of retweets: ' + str(tmp['tweet']['retweet_count'])
	print 'User ID: ' + str(tmp['tweet']['user']['id'])
	print 'User name: ' + str(tmp['tweet']['user']['name'])
	break
	

f.close()
