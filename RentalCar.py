# RentalCar Cost Estimator
# Program Must perform the following:
#		1. Collect customer input
#			a. Inputs:
#		2. Calculate the costs from input
#		3. Display the results to the user
#			a. Final Output:
#				Rental Code: D
#				Rental Period: 5
#				Starting Odometer: 1234
#				Ending Odometer: 2222
#				Miles Driven: 988
#				Amount Due: $422.00

# import literal eval module to test data types
from ast import literal_eval
import ast

#### Helper Functions ####
# Method used for rentalCode Input Validation
def checkRC(rc):

	# Prompt user for correct input if needed
	while True:
		# test rc input validity
		if rc == "B" or rc == "D" or rc == "W" or rc == "b" or rc == "d" or rc == "w":
			break

		# Prompt user for correct input and store in rc variable
		rc = input("Please enter (B), (D), or (W) to select the correct Rental Code. ")

	# test for lowercase
	if rc == "b" or rc == "d" or rc == "w":
		rc = rc.upper()

	# return rentalCode
	return rc

# Method used for rentalPeriod Input Validation
def checkInt(num):
	# Loop through input to validate data
	while True:
		# Try to convert num to int
		try:
			num = int(num)
			# if num greater than 0
			# then break and reurn num as an int
			if num > 0:
				break
			# else prompt user to enter a num greater than 0
			else:
				num = input("Please enter number greater than zero: ")
		# if try fails catch error
		# and prompt user to enter a number and not a str
		except ValueError:
			print("This is not an int!")
			num = input("Please enter number greater than zero and not a letter: ")
	# output and return the rentalPeriod
	return int(num)

# Check that Ending Odo is greater than Start Odo
def checkOdomEnd(odomEnd, odomStart):
	while True:
		# check the validity of odomEnd
		# dont need to check odomStart because it
		# should be using checkInt before being passed into function
		odomEnd = checkInt(odomEnd)
		# odomEnd > odomStart than exit and return odomEnd
		if (odomEnd > odomStart):
			break

		# If odomEnd is < odomStart prompt user for new input
		odomEnd = input("Please enter number greater than " + str(odomStart) + ": ")
	return int(odomEnd)

#### Main Program ####
# Rental Code Pricing Values
budgetPrice = 40.00
dailyPrice = 60.00
weeklyPrice = 190.00

# Request User Input and store in rentalCode
rentalCode = input("\n(B)udget, (D)aily, or (W)eekly rental? ")

# Validated rentalCode input
rentalCode = checkRC(rentalCode)

# Prompt user for rental period in days or weeks
if rentalCode == "D":
	daysRented = input("Number of Days Rented: ")
	# function to checkRP(rentalPeriod)
	rentalPeriod = checkInt(daysRented)

	# Check the Starting Odometer and set value to OdoStart
	OdoStart = checkInt(input("Starting Odometer Reading: "))

	# Check the End Odometer and set value to OdoEnd
	OdoEnd = checkInt(input("Ending Odometer Reading: "))
	OdoEnd = checkOdomEnd(OdoEnd, int(OdoStart))
	print("\n")

	milesDriven = OdoEnd - OdoStart
	# Apply pricing to Miles
	# $0.25 per Mile
	# Calculate Avg Day Miles
	avgMilesDay = milesDriven / int(rentalPeriod)

	# if avg miles per day is greater than 100
	# then find the extra miles driven and
	# multiply by $0.25 to find total charge
	if avgMilesDay > 100:
		extraMiles = (avgMilesDay - 100) * rentalPeriod
		milesCharge = (extraMiles) * 0.25

	# Apply pricing to rentalPeriod
	totalDue = (rentalPeriod * dailyPrice) + milesCharge

elif rentalCode == "W":
	weeksRented = input("Number of Weeks Rented: ")
	# function to checkRP(rentalPeriod)
	rentalPeriod = checkInt(weeksRented)

	# Check the Starting Odometer and set value to OdoStart
	OdoStart = checkInt(input("Starting Odometer Reading: "))

	# Check the End Odometer and set value to OdoEnd
	OdoEnd = checkOdomEnd(checkInt(input("Ending Odometer Reading: ")), OdoStart)
	print("\n")

	milesDriven = OdoEnd - OdoStart
	# Apply pricing to miles
	# $0.25 per Mile
	# Calculate avg miles
	avgMilesWeek = milesDriven / int(rentalPeriod)

	# if avg miles per week is greater than 900
	# then charge $100.00 / week
	if avgMilesWeek > 900:
		milesCharge = rentalPeriod * 100.00
	else:
		milesCharge = 0

	# Apply pricing to rentalPeriod
	totalDue = (rentalPeriod * weeklyPrice) + milesCharge

# Output Rental Code & Rental Period
print("Rental Code: " + rentalCode)
if rentalCode != 'B':
	print("Rental Period: " + str(rentalPeriod))
else:
	print("Rental Period: Budget Rentals don't have a Period.")

	# Check the Starting Odometer and set value to OdoStart
	OdoStart = checkInt(input("Starting Odometer Reading: "))

	# Check the End Odometer and set value to OdoEnd
	OdoEnd = checkOdomEnd(checkInt(input("Ending Odometer Reading: ")), OdoStart)
	print("\n")

	milesDriven = OdoEnd - OdoStart
	# Apply pricing to Miles
	# $0.25 per Mile
	milesCharge = (milesDriven) * 0.25
	# Apply pricing to rentalPeriod
	totalDue = budgetPrice + milesCharge


print("Starting Odometer: " + str(OdoStart))

print("Ending Odometer: " + str(OdoEnd))

print("Miles Driven: " + str(milesDriven))

# Apply Base Charge
precison = 2
width = 4
print(f"Amount Due: ${totalDue:{width}.{precison}f}")










