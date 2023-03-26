list = ["a", "b", "c", "d", "e", "f"]
print({i: j for i, j in enumerate(list, 0)})

print("start code")
list1 = ["sunny ", "gaikwad", "shubham", "kad", "vaibhav", "bharate"]
print({i: j for i, j in enumerate(list1, 0)})

t = [10, 20, 30]
print({i:j for i, j in  enumerate(t, 0)})

print("*"*100)
list_2=[10,20,30,40,50]
count=0
d=int(input("acces item you want:"))
for i in range(list_2):
    if list_2[i] == d:
        continue
    count=count+1
print("frequency is:",count)