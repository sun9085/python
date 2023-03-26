"""natural number satart from 0"""
"""
# you can print natural numbers from 0 to n and sum of all this numbers
n=int(input("enter number:"))
if n<0:
    print("enter positive number please:")
else :
    sum=0
    while n>0:
        sum+=n
        n-=1
        print("sum:",sum)


# you can print natural numbers from 1 to end numbers 

m=int(input("enter numbe"))
for i in range(1,m+1):
    if i<0:
        print("enter pstv number")
    else:
        print("natural number:",i)

"""
print("natural numbers 0 to n  print there sum also")
n=int(input("enter number:"))
if n < 0:
    print("plaesse enter the positive number:")
else:
    sum=0
    while n>0:
        sum+=n
        n-=1
        print("sum of natural number is :",sum)

