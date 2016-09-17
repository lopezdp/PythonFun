#Write a method not_string which takes a string and returns that
#string with the word "not " prepended to it UNLESS the original
#string already begins with the full word "not ".

#For example:
    
#not_string("Hi, this is a string")
#=>  "not Hi, this is a string"

#not_string("not a string here")
#=> "not a string here"

#not_string("nothing strange about this one")
#=> "not nothing strange about this one"


def not_string(s):
    if(s[0:3] == "not"):
        print s

    else:
        n = "not "
        print n + s








