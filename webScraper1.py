#David P. Lopez
#Web Scraper 

import urllib
from BeautifulSoup import * 

#prompt user for link
url = raw_input('Enter Link to Scrape: ')
html = urllib.urlopen(url).read()

#parse html with beautiful soup
pgContent= BeautifulSoup(html)

#find all span tags
spanTags = pgContent('span')

sum = 0

#loop through span tags and sum numbers
for span in spanTags:
	num = int(span.contents[0])
	sum += num

#print sum
print sum
