print("start code")

a=[]
size=int(input("enter size :"))
for i in range (size):
    x=input("add item in list:")
    a.append(x)
d=input("enter finding item frequency in list:")
count=0
for i in range(size):
    if a[i]==d:
        count=count+1
print("frequency item in list is:",count)