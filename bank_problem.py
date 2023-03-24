#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to the bank")
name=input("May I have your name?")
ac_no=int(input("May I have your account number?"))
ac_bal=int(input("Please enter the account balance:-"))
choice=int(input("Choice 1 for credit and 2 for debit"))
print("Initial account balace of",ac_no,"with name",name,"is:-",ac_bal)
transaction=int(input("Enter the amount:-"))
if choice==1:
    new_bal=ac_bal+transaction
else:
    new_bal=ac_bal-transaction
print("Thanks for choosing the bank!")
print("Transaction is completed",new_bal,"is updated balance.")


# In[ ]:


age=int(input("How many years you old are:-"))
nationality=input("Which nation you are belongs from:-")
stay_time=int(input("How many years you have been staying in india:-"))
if age>=18 and nationality=="indian":
    if stay_time>=5:
        print("You are eligible for voting!")
    else:
        print("You need to spend",5-stay_time,"years in India to eligible for voting")
else:
    print("You are not eligible for voting!")


# In[ ]:


age=int(input("How many years you old are:-"))
if age>=18:
    nationality=input("Which nation you are belongs from:-")
    if nationality=="indian" or nationality=="Indian":
        print("Congratulations!You are eligible for voting")
    else:
        stay=input("Enter your current location:-")
        if stay=="India" and stay="india":
            print("How many years you had been staying in india?")
            if years>=5:
                print("Congratulations you are eligible for voting")
            else:
                print("You are not eligible for voting")
        else:
            print("You are not eligible for voting")
else:
    print("Sorry but you are not eligible for voting")


# In[ ]:


num=int(input("Enter the number:-"))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")


# In[ ]:


s=[1,2,3,4,5,6,7,8,9,10]
for i in s:
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")


# In[ ]:


i=1
while i<=10:
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
    i=i+1


# In[ ]:


#Average number
n=int(input("Total no of values you want to enter:-"))
sum=0
for i in range(n+1):
    sum+=i
average=sum/n
print("Average of the first n natural numbers is:-",average)


# In[ ]:


for i in range(1,20,3):
    print(i)


# In[ ]:


l1=[]
sum=0
n=int(input("Enter no of iterations:-"))
print("Enter the numbers:-")
for i in range(n):
    num=int(input())
    l1.append(num)
print(l1)
for i in l1:
    sum+=i
print("Sum of numbers are:-",sum)
print("Number of iterations are:-",n)
average=sum/n
print("Average of the numbers is:-",average)


# In[ ]:


n=int(input("Enter no of iterations:-"))
count=0
sum=0
print("Enter the numbers:-")
while count<n:
    num=int(input())
    sum+=num
    count+=1
print("Sum of numbers are:-",sum)
print("Number of iterations are:-",n)
average=sum/n
print("Average of the numbers is:-",average)


# In[ ]:


#Average number
n=int(input("Total no of values you want to enter:-"))
sum=0
for i in range(1,n,2):
    sum+=i
    print(i)
average=sum/n
print("Average of the first n natural numbers is:-",average)


# In[ ]:


#Factorial
num=int(input("Enter the number which for factorial:-"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of",num,"is:-",fact)


# In[ ]:


#Factorial
num=int(input("Enter the number which for factorial:-"))
fact=1
count=1
while count<=num:
    fact=fact*count
    count+=1
print("Factorial of",num,"is:-",fact)


# In[ ]:


num=int(input("Enter the number:-"))
if num>=10:
    for i in range(num+1):
        if i%2!=0:
            print(i)
else:
    print("Number below 10 are not accepted")

