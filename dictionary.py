"""
dictionary : mutable data type , hetrogenous , key and value pair   , key must be  unique ,  we can use  repeat values ,

"""
dictionary={1:10,2:20,3:40,4:50,5:60,6:70}
print(dictionary)

""" if  add element  in  dictionary  use  direct                                                   1> dict[key_name]=value     """
dictionary[7]=90
dictionary[8]=100
dictionary[9]=120
dictionary[10]=130
dictionary[11]=140
print(dictionary)

""" if you want to update or change value of keys then use update method:                           2> d.update({key_name:value})   """
dictionary.update({1:"sunny"})
dictionary.update({2:"godrej"})
dictionary.update({3:"modi"})
dictionary.update({4:"ranjnath_singh"})
print(dictionary)

""" if you want print all keys in dictionary use d.keys() meyhod                                     3> d.keys()                     """

print(dictionary.keys())

""" if you want to print all values in dictionary use values method                                 4> d.values()                  """

print(dictionary.values())

""" if you want get specific value of key use get method                                             5> d.get(key_name)              """

print("get:value :",dictionary.get(1))
print("get:value :",dictionary.get(2))
print("get:value :",dictionary.get(3))
print("get:value :" ,dictionary.get(4))

""" if you want remove last element in dictionary use popitem() method                                6> d.popitem()                 """

print("use popitem remove last_element inform of tuple :",dictionary.popitem())
print("use popitem remove last_element  inform of tuple :",dictionary.popitem())
print("use popitem remove last_element  inform of tuple :",dictionary.popitem())

print(dictionary)

""" if yoy want remove specific key & value pair in dictionary user pop()method                        7> d.pop(key_name)               """

# remove 8th and 7th element in dictionary
print("remove key & value pair in dictionary:",dictionary.pop(8))
print("remove key & value pair in dictionary:",dictionary.pop(7))

""" if you are  add  value without key_name  only value is add absent key name 
setdefault() method
                                                                                                       8> d.setdefault() """
d={1:22,2:55}
d.setdefault('',45)
print("keyname_empty but value is add:",(d))

""" if you want delete all key & value pairs in dictionary use clear method                            9> d.clear()        """

""" if you want to copy dictionary use copy() method                                                   10> d.copy()         """