

# how to add element in empty list :

# create empty list:
l=[]
# how many element you want to add in empty list;
n=int(input("enter how many elements you want to add in empty list:"))
# for loop lavane:
for i in range(0,n):
    a=int(input("enter adding element in empty list:"))
    l.append(a)
print("newly created list:",l)
for x in l:
    print("square of newly careated items:",x**2)




# conacatenating two list :


list1=[10,20,30]
list2=[14,45,63]
list3=list1+list2
print(list3)
print("square in all list3:")
for i in list3:
    print(i**2)

print("print cube of all elemnts in list3:")
for i in list3:
    print(i**3)

# how to  add two string in list;

l=[]
n=int(input("to n element:"))
for i in range(0,n):
    a=input("enter string:")
    l.append(a)
print("list:",l)

l1=[]
l2=[]
n=int(input("enter total num items in list;"))
for i in range(0,n):
    x1=input("ent list1 element str:")
    l1.append(x1)
print("list1",l1)
