
# prime numbers


n=int(input("enter number:"))

if n>1:
    print("ist prime number")
elif n==0:
    print("its not prime number")
else:
    print("end code")



# odd and even number:


num=int(input("enter num:"))
if num%2==0:
    print("even number")
else:
    print("odd number")



n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print("facctorial:",fact)

