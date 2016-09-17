#2. FlimFlam 
#Write a method flimflam which prints all the numbers from 1 to 100 with a
#few exceptions:
    
#If the number is a multiple of 3, instead print "FLIM". 
#If the number is a multiple of 5, instead print "FLAM" 
#If the number is a multiple of both 3 and 5, instead print "FLIMFLAM"


#Note: The "modulo" operator, `%`, returns the remainder when two numbers
#are divided, for instance 8 % 6 #=> 2

#FlimFlam in action: 
#flim_flam()
#1
#2
#FLIM
#4
#FLAM
#FLIM
#7
#...


def flimflam():
    count = 1;
    lst = []
    
    while(count !=101):
        lst.append(count)
        count = count + 1
        
    for num in lst:
        if(num % 3 == 0 and num % 5 == 0):
            print "FLIMFLAM"
        elif(num % 5 == 0):
            print "FLAM"
        elif(num % 3 == 0):
            print "FLIM"
        else:
            print lst[num - 1]


        
    


















