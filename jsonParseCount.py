import urllib
import json

serviceUrl = raw_input("Enter URL to parse:")

if len(serviceUrl) < 1 : 
	serviceUrl = "http://python-data.dr-chuck.net/comments_253621.json"

sum = 0

data = urllib.urlopen(serviceUrl).read()

info = json.loads(str(data))

print json.dumps(info, indent = 4)

for item in info['comments']:
	cnum = item['count']
	sum = sum + cnum

print sum
