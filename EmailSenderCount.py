#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number
#of mail messages.

#The program looks for 'From ' lines and takes the second word
#of those lines as the person who sent the mail.

#The program creates a Python dictionary that maps
#the sender's mail address to a count of the number of times
#they appear in the file.

#After the dictionary is produced, the program reads
#through the dictionary using a maximum loop to find the
#most prolific committer.

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

counts = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    #print words
    for word in words[1]:
        if words[1] not in counts :
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1
            
for key in counts:
        print key, counts[key]
