#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. WAP to print even numbers from 121 to 229 using for loop. 

for i in range(121,229):
    if i%2==0:
        print("even number:",i)
 


# In[ ]:


# 2. WAP to print odd numbers from 521 to 229 using while loop

for x in range(229,512):
    if x%3==0:
        print("odd numbers:",x)


# In[ ]:


# 3. WAP to show the use of break statement ( in for loop)

for x in range(0,50):
    if x==15:
        break
print(x)
    


# In[ ]:



# 4. WAP to find GCD and LCM of given number?

m=int(input("enter number_m:"))
n=int(input("enter number_n:"))
d=min(m,n)
while True:
    if m%d==0 and n%d==0:
        print("find number is gdc :",d)
        break
    else:
        d=d-1
lcm=m*n/d
print("lcm is :",lcm)


# In[ ]:


# 5.Write a Python program to print all alphabets from a to z using for loop

alphabets=[ 'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S','T' ,'U', 'V', 'W', 'X', 'Y','Z' ]

for x in alphabets:
    print(x)


# In[ ]:


# 6.Write a Python program to find sum of all even numbers between 1 to n.

n=int(input("enter numbers :"))
sum=0
for i in range(1,n+1,1):
    if i%2==0:
        sum=sum+n
        print("sum are :",i,"sum is :",sum)


# In[ ]:


# 7.Write a Python program to find sum of all odd numbers between 1 to n
n=int(input("enter numbers :"))

sum=0
for x in range(1,n+1,1):
    if x%2!=0:
        sum=sum+n
        print("odd num is:",n,"sum is :",x)


# In[ ]:


#8. Write a Python program to count number of digits in any number
n=int(input("enter number:"))
count=0
while n !=0:
    n//=10
    count+=1
print("number in digits are:",count)


# In[ ]:


# 9. Write a Python program to calculate product of digits of any number
u=int(input("enter number is:"))
b=u*(u)
print("product of any number is :",b)


# In[ ]:


# 10. Write a Python program to find frequency of each digit in a given integer.
n=int(input("enter number is:"))
l=[]
l.append(n)
count=0
while n<=0:
    n+=1
    count+=1
    print("digit count")
print(l)
print(count)
    


# In[ ]:


#10. Write a Python program to find frequency of each digit in a given intege
num=input("enter num")
d=input()
c=0
for i in num:
    if i==d:
        c=+1
print(c/len(num))        


# In[ ]:


# 11. Find all prime number between 400 to 300;
numx=400
numy=300
for a in range(numx,numy+1):
    for i in range(2,a):
        if a%i==0:
            break
        else:
            print(a)


# In[ ]:


#12. WAP to print table of given no
n=int(input("enter number:"))
for i in range(1,11):
    print((n*i))


# In[ ]:


#13. WAP to print squares from 1 to20
n=1

while n<=21:
    print("sq:",(n*n))
    n=n+1
   


# In[ ]:


#14. WAP to accept base and index from user and calculates power
b=int(input("enter num"))
ind=int(input("enter num"))
power=b**ind
print(power)


# In[ ]:


# 15. 1!+2!+3!.........+n! find s (factorial problem)
n=int(input("entr num:"))
f=1
s=0
for i in range(1,n+1):
    f=f*i
    s=s+f
print("factorial is:",f)
print("sum:",sum)


# In[ ]:


# 16. WAP to check given no is Krishnamurthy or noteg) 153=1!+5!+3!=153
# Python program to check if the number is an Armstrong number or not


num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[ ]:


#17. WAP to check given no is palindrome or not. Original =ReverseEg 1221?
     
def isPalindrome(s):
    return s == s[::-1]
s = input("enter palindrome word:")            ## malyalam 
ans = isPalindrome(s)                          ## ana                          
if ans: 
        print("Yes")
else:
    print("No")     


# In[ ]:


#18. WAP to check given no is automorphic or notinput n=2 output Automorphicas 25*25=625?

num1=int(input("enter num:"))
num2=num1
sq=num1*num2
print("num1 is:",num1)
print("sq  is :",sq)
num1=str(num1)
sq=str(sq)
if sq.endswith(num1):
    print("enter number is automorphic :")
else:
    print("enter number is not automorphic")


# In[ ]:


#19. WAP to find given number is Harshad/Niven number or not?


# In[ ]:


# 20. Print all palindrome numbers from 100 to 500?
for number in range(100,500):
        var=number
        reverse=0
        while number>0:
            digit=number%10
            reverse=reverse*10+digit
            number=number//10
        if var==reverse:
            print("var",var)
        


# In[6]:


# Python program to check
# if a number is Harshad
# Number or not.
n=int(input("enter number:"))
def checkHarshad( n ) :
	sum = 0
	temp = n
	while temp > 0 :
		sum = sum + temp % 10
		temp = temp // 10
	# Return true if sum of
	# digits is multiple of n
	return n % sum == 0

# Driver Code
if(checkHarshad(n)) : print("Yes")
else : print ("No")

if (checkHarshad(n)) : print("Yes")
else : print ("No")
	
# This code is contributed
# by Nikita Tiwari


# In[ ]:




