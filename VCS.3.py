#Write a method no_dupes which will take an array and returns
#that same array with all duplicate items removed.
#Assume integers.

#No Dupes in action: 
#no_dupes( [ 1, 4, 2, 7, 3, 1, 2, 8 ] )
#=> [ 1, 4, 2, 7, 3, 8 ]

#no_dupes( [ 100, 32, 44, 44, 23, 32, 44 ] )
#=> [ 100, 32, 44, 23 ]

def no_dupes(lst):
    new_list = []

    for item in lst:
        if(item not in new_list):
            new_list.append(item)    

    for i in new_list:
        print i
        
    








        
    


















