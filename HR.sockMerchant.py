n = input()
sockArr = map(int, raw_input().strip().split(' '))
used = []
multCounts = []
last = 0
pairCount = 0

sockArr.sort()

print sockArr

for i in xrange(n):
  if(sockArr.count(sockArr[i]) > 1):
    used.append(sockArr[i])
    
for i in xrange(len(used)):
  if(used.count(used[i]) > 1 and last != used[i]):
    multCounts.append(used.count(used[i]))
    last = used[i]
for i in xrange(len(multCounts)):
  if(multCounts[i] % 2 == 0):
    pairCount += (multCounts[i] / 2)
  else:
    pairCount += ((multCounts[i] - 1) / 2)
    
print pairCount



