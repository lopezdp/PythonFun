#first line of input int n denoting number of commands
n = input()

#list of commands
cmdList = []
numList = []

#each line i contains one of the commands defined by n

for i in xrange(n):
  cmdList.append(raw_input().split())
  if(cmdList[i][0] == "insert"): #insert nums to list @ pos
    numList.insert(int(cmdList[i][1]), int(cmdList[i][2]))
  elif(cmdList[i][0] == "print"): #print numList
    print (numList)
  elif(cmdList[i][0] == "remove"): #remove nums from list
    numList.remove(int(cmdList[i][1]))
  elif(cmdList[i][0] == "append"): #append nums from list
    numList.append(int(cmdList[i][1]))
  elif(cmdList[i][0] == "sort"): #sorts list
    numList.sort()
  elif(cmdList[i][0] == "pop"): #pop last from list
    numList.pop()
  elif(cmdList[i][0] == "reverse"): #reverse list
    numList.reverse()


