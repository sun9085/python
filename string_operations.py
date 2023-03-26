# reverse string in by using square barsess
print("reverse string :")

string="sunny chandrakant gaikwad"
print(string[::-1])

print("*"*100)

# slicing string operation in string
print("printing negative indexing of string s:")
s="sunny"
a=s[-1]           # PRINT LAST CHARCATOR FROM STRING
b=s[-2]           # 2ND LAST CHRACATOR  FROM STRING
c=s[-3]           # LAST 3RD CHARACTOR FROM STRING
d=s[-4]           # LAST 4 TH CHARACTOR FROM STRING
print(a)
print(b)
print(c)
print(d)
print("*"*100)

# charactor acessing by indexin start from 0 to end in regular form :

print("acessing charactor from string by indexing:")
d="python"
print(d[0])
print(d[1])
print(d[2])
print(d[3])
print(d[4])
print(d[5])

print("*"*100)

# format method in string
print("format method in string : joining two words of strig")

print("{} and {} are best palyer in our team".format("sunny","andy"))
print("{} and {} this two pepole are not live in india".format("jaysurya","rock"))
print("{} and {}  or mr.sharma are best freind forever ".format("salaman_khan","sharukh_khan"))
print("*"*100)
# postional argument passing in format ,method:
print("{0} and {1}  are best palyer in india.".format("virat","rohit"))

print("*"*100)

# key word argument in string

print("keyword argument in string like :{a},{b},{c}=(a=sunny,b=chandrakant,c=gaikwad")

print("{a},{b},{c}".format(a="sunny",b="chandrkant",c="gaikwad"))
print("{a},{b},{c}".format(c="sunny",a="chandrkant",b="gaikwad"))
print("*"*100)

# adding interger,string ,float value in string
print("adding string ,float,integer value in string")
integer=10
float=1.23
string="sunny"
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(integer,float,string))
print("*"*100)

print(" #short cut for adding integer %d ,string %s ,flaot %f in string")
a=1
b=1.2
c="rockstar"
print("mi integer %d ani mi float %f  va mi string %s"%(a,b,c))
print("*"*100)

## upper method : all charactor in upper format:
print("upper method : all charactor in upper format")
s="sunny gaikwad"
print(s.upper())

## lower method : all charactor in lower format :
print("lower method : all charactor in lower format :")
print(s.lower())

## capitalise method: initial world is capital :
print("capitalise method: initial world is capital :")
print(s.capitalize())

## split method : all charactor are in list format:
print("split method : all charactor are in list format:")
print(s.split())
## swapcase method : all charactor convert into upper  foramt:
print("swapcase method : all charactor convert into upper  foramt:")
print(s.swapcase())
## title method : each word initial is capital:
print("title method : each word initial is capital:")
print(s.title())








































































"""
# Variable declaration
str = "Javaisaprogramminglanguage"
# Calling function
str2 = str.partition("language")
print(str2)
"""