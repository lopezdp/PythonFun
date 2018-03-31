import urllib
import json

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input('Enter location: ')

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url

data = urllib.urlopen(url).read()

print 'Retrieved',len(str(data)),'characters'

jsfile = json.loads(data)

print json.dumps(jsfile, indent = 4)

pid = jsfile['results'][0]['place_id']

print "Place id: ", pid