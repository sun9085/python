# how to concatenate two list

# by adding two list by + opearator
list1=[1,2,3,4,5]
list2=[10,20.,30]
list3=list1+list2
print("concatenate two lists in new one:",list3)

i = 1
odd = []
even = []
while i < 11:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
    i += 1

print('The odd numbers are:')
for i in odd:
    print(i)

print('The even numbers are:')
for j in even:
    print(j)