
"""palindrome means miirror / arsa"""

# EXAMPLE STRING LIKE : MAM , MALYALAM ,MOM ,

string1="mam"
string2=string1[::-1]
if string1==string2:
    print("string is palindrome ")
else:
    print("string not palindrome")

print("*"*100)


stringx=input("enter string you want:")
stringy=stringx[::-1]
if stringx==stringy:
    print("entered string is palindrome")
else:
    print("not palindrome string you entered")
