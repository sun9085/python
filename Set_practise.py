#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Create a set of different products, add some more elements to it and print it.
set1={6,4,2,7,9}
print("The original set is:-"+str(set1))
set2=[1,5,10]
set1.update(set2)
print("Set after adding elements:-"+str(set1))


# In[17]:


#2.Given 2 different sets, access the elements from the set and print all elements from both set
set1={1,2,4,5,6,7,9,10}
set2={1,2,3,4,5,6,7,8}
#print(set1.)
#print(set2[6])
set3=set1.union(set2)
print(set3)


# In[6]:


#3.Given 2 different sets, create a 3rd set which is havinf all common elements from set1 and set2
set1={1,2,4,5,6,7,9,10}
set2={1,2,3,4,5,6,7,8}
set3=set1.intersection(set2)
print(set3)


# In[8]:


#4.Given 2 different sets, create a 3rd set with elements which are from set1 but not in set2
set1={1,2,4,5,6,7,9,10}
set2={1,2,3,4,5,6,7,8}
set3=set1.difference(set2)
print(set3)


# In[15]:


#5.Create a immutable set that holds primary key column values from employee table
emp_id={101,102,103,104,105,106,107,108,109,110}
emp_id_frozen=frozenset(emp_id)
print(emp_id_frozen)


# In[14]:


#6.Given a set with some elements.Add a tuple to this set
set1={1,2,3,4,5,6,7,8}
print(set1)
set1.add((1,2,3,))
print(set1)

