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
