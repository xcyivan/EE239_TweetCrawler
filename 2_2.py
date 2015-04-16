import urllib
import httplib
import json
import datetime, time



API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

hashtags=['#SB49','#football','#MakeSafeHappen','#brandbowl','#adbowl']


def transtime(hour, minute, second):
	hh = hour
	mm = minute
	ss = second*5
	start_date = datetime.datetime(2015,02,01, hh,mm,ss)
	ss = ss+5
	if ss == 60:
		ss = 0
		mm = mm+1
	if mm == 60:
		mm = 0
		hh = hh+1
	end_date = datetime.datetime(2015,02,01, hh,mm,ss)
	return [start_date, end_date]



def search(hashtag, start_date, end_date):
	mintime = int(time.mktime(start_date.timetuple()))
	maxtime = int(time.mktime(end_date.timetuple()))

	params = urllib.urlencode({'apikey' : API_KEY, 'q' : hashtag,
							   'mintime': str(mintime), 'maxtime': str(maxtime),
							   'new_only': '1', 'include_metrics':'1', 'limit': 500})

	req_url = url + '?' + params
	req = httplib.HTTPConnection(host)
	req.putrequest("GET", req_url)
	req.putheader("Host", host)
	req.endheaders()
	req.send('')

	resp = req.getresponse()
	if resp.status != 200:
		print "Connection error from " + start_date + "to " + end_date
		return None
	resp_content = resp.read()
	ret = json.loads(resp_content)
	tweets = ret['response']['results']['list'] # tweets is an Object
	if len(tweets) >= 500:
		print "No. of Results exceed maximum from " + start_date + "to " + end_date
		return None

	return tweets

	

file_t = open('tweets.txt', 'w')
file_log = open('search_log.txt', 'w')

group = 0
count = [0,0,0,0,0]
for hashtag in hashtags:
	for hour in range(10,15):
		for minute in range(60):
			print hashtag + ' ' + str(hour) + ':' + str(minute)
			for second in range(12):
				[start_date, end_date] = transtime(hour, minute, second)
				tweets = search(hashtag, start_date, end_date)
				count[group] += len(tweets)
				file_log.write(hashtag + '\tFrom: ' + str(start_date) + '\t\tTo: ' + str(end_date) + '\t\tNo. Of Results: ' + str(len(tweets)) + '\n')
				for tweet in tweets:
					tmp = json.dumps(tweet)
					file_t.write(tmp)
					file_t.write('\n')
				
	group += 1

file_t.close()
file_log.close()

for n in count:
	print n
