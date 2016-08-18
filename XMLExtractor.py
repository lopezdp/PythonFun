import urllib
import xml.etree.ElementTree as ET 

#prompt for link where xml data resides
#Use this link for testing: http://python-data.dr-chuck.net/comments_42.xml
#USe this link for actual: http://python-data.dr-chuck.net/comments_253617.xml

url = raw_input('Enter URL Link: ')
sum = 0

#open url and prep for parsing
data = urllib.urlopen(url).read()

#read url data and convert to XML Node Tree for parsing
comments = ET.fromstring(data)

#for loop to iterate through count nodes using .findall()
for counts in comments.findall('comments/comment/count'):
	#sum each node using counts.text method to extract value and typecast to int
	sum = sum + int(counts.text)

print sum







