arr = map(int, raw_input().strip().split(' '))

t1 = arr[0]
t2 = arr[1]
n = arr[2]

# 0, 
#1, 
#t1 = t2**2 = modFib
#0 + 1**2 = 1, 
#(t1 = t2) + (t2 = modFib)**2 = modFib
#1 + 1**2 = 2, 
#(t1 = t2) + (t2 = modFib)**2 = modFib
#1 + 2**2 = 5,
#2 + 5**2 = 27

for i in xrange(n - 2):
  modFib = t1 + t2**2
  t1 = t2
  t2 = modFib
  print modFib
