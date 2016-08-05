"""
program will use urllib to read HTML from a data file,
it will extract href= values from the anchor tags, scan 
for a tag that is in a particular position relative to 
the first name in the list, follow that link and repeat
the process and report the last name you find.

Find link at pos = 3 (first name is pos = 1). follow link, 
and repeat 4 times. Answer is last name you retrieve.   

"""

import urllib
from BeautifulSoup import *

# prompt user for page source
url = raw_input('Enter link to page: ')
#html = urllib.urlopen(url).read()
#pgContent = BeautifulSoup(html)

index = 0
pos = 0
lst = []

# prompt user for starting location & iterations
sPos = int(raw_input('Enter the starting position: '))
repeat = int(raw_input('How many repetitions?: '))



for link in range(0,repeat):
	# Retrieve all of the anchor tags and append links to lst[]
	html = urllib.urlopen(url).read()
	pgContent = BeautifulSoup(html)
	tags = pgContent('a')
	for tag in tags:
		lst.append(tag.get('href', None))
		index = index + 1
	# assign link to follow to url
	url = lst[sPos - 1]
	print url
	# clear list
	lst = []





	
