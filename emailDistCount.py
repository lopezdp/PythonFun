#10.2 Write a program to read through the mbox-short.txt
#and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time
#and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour,
#print out the counts, sorted by hour as shown below.

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"

#open file and assign to fhand
fh = open(fname)

#create dictionary to keep track of email count sent for each hour
counts = dict()

#loops through each line in file
for line in fh:
    line = line.rstrip() #strips each line of the \n charachter
    if not line.startswith('From '): continue #disregards lines with no 'From ' and continues
    words = line.split() #creates a lists that contains each word in the 'From ' line
    w5 = words[5] #isolates the time we are interested in
    w5SPL = w5[0:2] #isolates the hour of interest
    #counts the distribution of each hour and puts in count{}
    counts[w5SPL] = counts.get(w5SPL, 0) + 1 

#print counts
#create a list to store and sort dict() items
lst = list()

#loop through dictionary and append to lst
for k, v in counts.items():
    lst.append((k, v))

#reverse sort lst
lst.sort()
#print lst

#print lst
for k, v in lst:
    print k, v
