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

	currentInt = 0 # Place holder for the current integer to test
	currentSequence = 0 # Place holder for the current sequence of HappyNums Found
	foundAHappyNum = 0 # Holds the most recent HappyNum found

	happyLst = list() # list of all happyNums found in a given sequence

	while(currentSequence <= n): # tests for the current sequence to be tested
		if(isHappyNumber(currentInt)): # verifies if currentInt is a happyNum
			foundAHappyNum = currentInt # holds any HappyNum found in a given sequence
			happyLst.append(foundAHappyNum) # adds all happyNums to a list to access later
			currentInt += 1 # increments the currentInt being tested
			currentSequence += 1 # increments the currentSequence of happyNums that have been found
			if(currentSequence == n): # inefficient redundancy
				break # breaks out of loop if sequence is == to n sequence we are looking for
		elif(not(isHappyNumber(currentInt))): # if isHappyNumber is False then executes next codeBlock
			currentInt += 1 # increments currentInt to be tested next

	return happyLst[n-1] # returns the happyNum for the given sequence we are looking for















  

