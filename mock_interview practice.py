# how to add element in empty list
"""
n=int(input("enter how many item add in list:"))
list1=[]
for i in range(0,n):
    a=int(input("enter item in list:"))
    list1.append(a)
print("new list:",list1)

print("*"*100)

# how to add in element in empty tuple

n=int(input("enter no item add in tuple:"))
l=[]
for i in range(0,n):
    a=int(input("enter element:"))
    l.append(a)
print("new_tuple is:",tuple(l))

print("*"*100)

# how to add element in  empty set

n=int(input("enter total item:"))
l=[]
for i in range(0,n):
    a=int(input("enter item:"))
    l.append(a)
print("new_set :",set(l))

print("*"*100)

# find how many charactor in string

string=input("enter string:")
a=list(string)
freq=(a.count(x) for x in a)
d=dict(zip(a,freq))
print(d)

print("*"*100)


# how to know sring is palindrome or not
string1=input("enter your string:")
string2=string1[::-1]
if string1==string2:
    print("enter string is palindrome-like mirror")
else:
    print("enter string not palindrome")

print("*"*100)


# how find two string are anagarm or not


#angarm string :  string1  and string 2 conatins similar charctor  not in ordeded

 #example of :    1> abc -cab
  #                  2> speed -deeps
   #                 3> hert- eart
    #               5> spare- pears
     #               6> study-dusty

from collections import Counter
def anagram(string1,string2):

    if Counter(string1)== Counter(string2):
        print("anagram strings")
    else:
        print("not anagram strings")
anagram(string1=input("enter string1:"),string2=input("enter string2:"))

print("*"*100)


# print odd / even number  n th numbers

n=int(input("enter number:"))
for n in range(0,n+1):
    if n %2==0:
        print("even number",n)
    else:
        print("odd number",n)

print("*"*100)



# create class

class student:

    schoo_name="vidya bharti hindi  medium school"

    def __init__(self, name, age):
        self.name=name
        self.age=age



    def doing_study(self):
        print(self.name," is studying")

    def paly(self):
        print(self.name," is palying football")

student1=student("avinash",12)                    # obj 1
student2=student("jonny",11)                      # obj2
print("printing schol_bame with help of calss name")
print(student.schoo_name)
print(student1.name,student1.age)
print(student2.name,student2.age)
student1.doing_study()
student1.paly()
student2.doing_study()
student2.paly()
print(student1.schoo_name)
print(student2.schoo_name)

print("*"*100)

# pattern of starts printing in regular : downfrom
n=int(input("enter number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print('\n')

# ulta pattern in python : upward from

n=int(input("enter number:"))
for i in range(n,0,-1):               # only change in for loop ,range(n,0,-1)
    for j in range(1,i+1):
        print("*",end='')
    print('\n')



# how to remove odd charactor in gievn string

string=input("enter string;")
return_string=''
for i in  range  (len(string)):
    if i%2==0:
        return_string+=string[i]
print(return_string)

print("*"*100)
"""
#how to remove even charactor in gievn string

string=input("enter string:")
print(string)
return_str=''
for i in range(len(string)):
    if i%3==0:
        return_str=string[i]
print(return_str,i)