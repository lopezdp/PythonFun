import urllib
import xml.etree.ElementTree as ET 

#prompt for link where xml data resides
#Use this link for testing: http://python-data.dr-chuck.net/comments_42.xml

url = raw_input('Enter URL Link: ')

#open url and prep for parsing
data = urllib.urlopen(url).read()

#read url data and convert to XML Node Tree for parsing
comments = ET.fromstring(data)

counts = comments.findall('comments/comment/count')

print len(counts)

for count in counts:
    print 'count', count.find('count').text



