n = int(raw_input().strip())
sum = 0
arr = map(int,raw_input().strip().split(' '))

for x in xrange(n):
  sum += arr[x]

print sum
