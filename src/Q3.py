# Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 10
for i in range(n):
    str = ""
    if i <= n / 2:
        for j in range(i):
            str += "*"
    else :
        for j in range(n, i, -1):
            str += "*"
    print str
   
