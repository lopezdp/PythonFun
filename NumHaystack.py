#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

import re

file = open('\pythonDrChuckTestData.txt')
for line in file:
	line = line.rstrip()
	num = re.findall('[0-9]+', line)
	print num


