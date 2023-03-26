print("convert list element in key and value pair")
l=["sunnny","gaikwad","ms","dhoni"]
print({i:j  for i ,j in enumerate(l)})

print("convert list into string ")

week_days=["sun","mon","tue","wed","thus","fri","sat"]
string=" ".join(week_days)
print(string)

print("convert list into tuple ")
week_days=["sun","mon","tue","wed","thus","fri","sat"]
tuple_new=tuple(week_days)
print(tuple_new)

print("convert list into tuple")
week_days=["sun","mon","tue","wed","thus","fri","sat","mon","sun"]
set_form=set(week_days)
print(set_form)