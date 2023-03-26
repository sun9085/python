input_string=input("enter string here:")    # take user input string
input_string=input_string.lower()           # conver into lower
count=0                                     # count=0 initial
vowels="aoiue"                              # vowels="aouie"

for i in input_string:                      # use for loop in enter string
    if i in vowels:                         # jar i in vowels madhal asel tr count +1 kra
        count=count+1
print("vowels are:",count)                  # print vowels and coun outer for loop
