line = raw_input("Enter line to check :")
digitCount = 0
letterCount = 0

for ch in line:
    if ch.isdigit():
        digitCount+=1
    elif ch.isalpha():
        letterCount+=1
        
print "Number of digits : ", digitCount
print "Number of letters : ", letterCount
        
        