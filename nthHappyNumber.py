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

