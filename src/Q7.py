# Write a Python program to check the validity of password input by users.
# Validation :
#  At least 1 letter between [a-z] and 1 letter between [A-Z].
#  At least 1 number between [0-9].
#  At least 1 character from [$#@].
#  Minimum length 6 characters.
#  Maximum length 16 characters.

import re
passwd = raw_input("Enter your password : ")

isValidate = True

if (len(passwd) < 6 or len(passwd) > 16):
    isValidate = False
elif not re.search('[a-z]', passwd):
    isValidate = False
elif not re.search("[A-Z]", passwd):
    isValidate = False
elif not re.search("[0-9]", passwd):
    isValidate = False
elif not re.search("[~!@#$%^&*()_/+\:,./?<>]", passwd):
    isValidate = False
    
if isValidate:
    print "Password is correct"
else : 
    print "Wrong password"
