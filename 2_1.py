import urllib
import httplib
import json
import datetime, time


#########   create UNIX timestamps
start_date = datetime.datetime(2015,2,1, 10,0,0)
end_date = datetime.datetime(2015,2,1, 15,0,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

#########   set query parameters
params = urllib.urlencode({'apikey' : API_KEY, 'q' :'#SB49',
                           'mintime': str(mintime), 'maxtime': str(maxtime),
                           'new_only': '1', 'include_metrics':'1', 'limit': 5})



#########   create and send HTTP request
req_url = url + '?' + params
# print req_url
req = httplib.HTTPConnection(host)
req.putrequest("GET", req_url)
req.putheader("Host", host)
req.endheaders()
req.send('')


#########   get response and print out status
resp = req.getresponse()
print resp.status, resp.reason


#########   extract tweets
resp_content = resp.read()
ret = json.loads(resp_content)
tweets = ret['response']['results']['list'] # tweets is an Object
print len(tweets)

t_indent = json.dumps(tweets, indent=1)
t_origin = json.dumps(tweets)

f = open('top_tweets.txt', 'w')

for tweet in tweets:
	tmp = json.dumps(tweet)
	# print tweet['tweet']['retweet_count']
	# tmp = json.dumps(tweet, indent=1)
	f.write(tmp)
	f.write('\n')
	
f.close()
