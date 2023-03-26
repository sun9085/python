'''
string=input("enter string here:")
a=(list(string))
freq=(a.count(x) for x in a)
d=dict(zip(a,freq))
print(d)

'''
# find out freqvency of charactor in list
"""
string=input("enter string you want:")
a=(list(string))
freq=(a.count(x) for x in a)
d=list(zip(a,freq))
#d=dict(zip(a,freq))
print(d)


string=input("enter:")
a=(list(string))
freq=(a.count(x) for x in a)
d=dict(zip(a,freq))
print(d)
"""

# find factorial

n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial is:",fact)
