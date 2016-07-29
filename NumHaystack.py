#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

import re

file = open('C:\Users\David\OneDrive\Documents\Python\RandomScripts\pythonDrChuckTestData.txt')

sum = 0

for line in file:
	line = line.rstrip()
	num = re.findall('[0-9]+', line)
	for n in num:
		sum += int(n)

print sum


