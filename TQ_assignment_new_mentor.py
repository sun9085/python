"""
1)Ram needs to convey his regards to his friends
on friendship day he has almost 10 friends.
write a code for the above situation.
"""
# we can use for loop if ram conveys his message to his 10 friends at time.
print(" Q-1> answer below:")
for i in range(0,11):
    print("happy friendship day:",i)
print("*"*50)

"""
2)Sita has scored good marks in exam..
according the marks secured by sita check
what grade she baged..
85+ distinction, 75-85 - first class , 65-75 second class.
except the marks from the user

"""
print("Q-2 : anser below:")

marks=int(input("enter marks of sita:"))

if marks >=85:
    print("sita got distinction")
elif marks >=75:
    print("sita got firstcalss")
elif marks >=65:
    print("sita got secondclass")
elif marks >=40:
    print("sita is passed")
else:
    print("thak you for enter marks!")

print("*"*50)
'''
3)Using nested for loop print the pattern
**
***
****
*****
******
'''
print("Q-3 answer below:")

for i in range(1,6):
     for j in range(1,i+1):
         print('*',end="")
     print("\n")

print("*"*50)

'''
4)Write a Python program which accepts the user's first and last name and
print them in reverse order.
'''
print("Q-4 answer below:")

first_name=input("enter your first name:")
last_name=input("enter your last name:")
a=list(first_name[::-1])
b=list(last_name[::-1])
print(a)
print(b)

print("*"*50)

'''
5)Write a Python program to get a new string from a given string where
"Is" has been added to the front. If the given string already begins with
"Is" then return the string unchanged



'''
'''
6)Display Fibonacci series up to 10 terms
'''
print("Q-6 answer below:")
def fibo (n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
n=int(input("from user:"))
if n <=0:
    print("enter positive number:")
else:
    for i in range(n):
        print(fibo(i))

print("*"*50)

'''
7)Explain List type in detail with example. also give atleast 3 methods
used with list.
'''
print("list is container data type which we can store hetrogenius data types like ,inter,string,tuple,boolean,flaotvalues")
print("list is container data type which we can store hetrogenius data types like ,inter,string,tuple,boolean,flaotvalues")
my_list=[10,20,"hii","buy"]
print(my_list)
my_list.append(88)         ## add element at last position
print(my_list)
my_list.pop()             ## remove last element in list
print(my_list)
my_list.sort()             ## sort in ordered data
print(my_list)

print("*"*50)

'''
8)Explain dictonary in detail with example. also demonstrate how to add,
remove and access the element from a dictionary.
'''
print("dict is hetrogenius data type,its contain key and value pair,key must be uniqe ,value of dict can be allow,"
      "we can upadte ,pop,remove,element in dict.")
dict1={1:100,"m":200,3:1.1,4:"amit"}
print(dict1)
print(dict1.keys())    # print all keys in dict1
print(dict1.values())  # print all values in dict1
print(dict1.pop(3))    # remove key&value pair in dict1
print(dict1.get(1))   # get value of key
dict1[15]="bachhan"   ## add key and value pair in dict1
print(dict1)
print(dict1.pop("m")) ## we can call value by use with key

print("*"*50)

'''
9)Define SQL and what are the different language statements in SQL.
Give the basic syntax for - creating table, inserting data to the table.
'''
print("sql - is structural query language ")
print("we can save and access data with help of sql ")
print("type pf language are blow:")
print("data manupulation language: insert,upadte,delete")
print("data defination language:create,drop,alter,truncate")
print("data control language: postitioning data:commit,rollback")
print("data query language:select data:")

'''
syntax : 
sqlplus hr/hr
create table xyz (name varchar(20),id number(5),address varchar(20),mobile number(10));
insert into xyz values("aman",1515,"pune",9260315572);
select * from xyz
we can perform operation :concat column ,user (airthmetic operation:+,-,*)  ,insrt,rollback,commit,all this operation in sql tables          

'''

'''
Q-10)Give difference between List tuple and set
'''

'''

         parameter     list             tuple

      1> speed         less             fast
      2> braket        []               ()
      3> methods       more             less
      4> data          hetrogenius      hetrogenius
      5> space         more             less


'''