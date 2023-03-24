# len - string, list, dict
# reversed

my_list = [1, 2, 3, 4, 5, "str"]
my_str = "RandomString"
print(len(my_list))
print(len(my_str))

print(list(reversed(my_list)))
for i in reversed(my_str):
    print(i)

s1 = "Hello "
s2 = "World"
s3 = s1 + s2
print(s3)

a = 1
b = 2
c = a + b
print(c)