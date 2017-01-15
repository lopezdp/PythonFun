def sumOfSquaresOfDigits(n):
	s = 0
	if(n <= 0):
		return n
	else:	
		strN = str(n)
		strL = len(strN)
		digit = ""
		tempIntDigit = 0

		for digits in range(strL):
			digit = strN[digits:digits+1]
			tempIntDigit = (int((digit)))**2
			s += tempIntDigit
		return s

def isHappyNumber(n):
	# Starting with any positive integer n, replace the number n by the sum of the squares of its digits, 
	# and repeat the process until the number either equals 1 (where it will stay)

	# or it loops endlessly in a cycle that does not include 1 

	# Those numbers for which this process ends in 1 are happy numbers, 
	# while those that do not end in 1 are unhappy numbers (or sad numbers). test idk

	firstHappyNum = int(n)  
	happyNumBool = False

	if(n <= 0):
		return happyNumBool
	else:  
		while(firstHappyNum != 1):
			if(sumOfSquaresOfDigits(firstHappyNum) == 1):
				break
			else:
				firstHappyNum = sumOfSquaresOfDigits(firstHappyNum)
			
			if(sumOfSquaresOfDigits(firstHappyNum) == 4):
				break
			else:
				continue

		if(sumOfSquaresOfDigits(firstHappyNum) == 1):
			happyNumBool = True

		return happyNumBool

def nthHappyNumber(n): 
	# ****n == sequence and != to to a happy num
	# input is sequence number 2
	# create loop and call function to create sum of squares 
	# count each loop that finds a happynum
	# if sum of squares == happy num then append to list through sequence num = 2
	# create all happy nums through sequence 2
	# return happy num pertaining through sequence 2

	currentInt = 0 # 
	currentSequence = 0 # 
	foundAHappyNum = 0 # 

	happyLst = list() # 

	while(currentSequence <= n): #

		if(isHappyNumber(currentInt)): #

			foundAHappyNum = currentInt #
			happyLst.append(currentInt) #
			currentInt += 1 #
			currentSequence += 1 #

			if(currentSequence == n): # 
				break #

		elif(not(isHappyNumber(currentInt))): #
			currentInt += 1 #

	return happyLst[n-1]















  

