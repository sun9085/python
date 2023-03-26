print("dict is hetrogenius data type,its contain key and value pair,key must be uniqe ,value of dict can be allow,"
      "we can upadte ,pop,remove,element in dict.")
dict1={1:100,"m":200,3:1.1,4:"amit"}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.pop(3))
print(dict1.get(1))
dict1[15]="dog"
print(dict1)
print(dict1.pop("m"))

print("*"*50)

'''
9)Define SQL and what are the different language statements in SQL.
Give the basic syntax for - creating table, inserting data to the table.
'''
print("sql - is structural query language ")
print("we can save and access data with help of sql ")
print("type pf language are blow:")
print("data manupulation language: insert,upadte,delete")
print("data defination language:create,drop,alter,truncate")
print("data control language: postitioning data:commit,rollback")
print("data query language:select data:")

'''
syntax : 
sqlplus hr/hr
create table xyz (name varchar(20),id number(5),address varchar(20),mobile number(10));
insert into xyz values("aman",1515,"pune",9260315572);
select * from xyz
we can perform operation :concat column ,user (airthmetic operation:+,-,*)  ,insrt,rollback,commit,all this operation in sql tables          
      
'''

'''
Q-10)Give difference between List tuple and set
'''

'''

         parameter     list             tuple
         
      1> speed         less             fast
      2> braket        []               ()
      3> methods       more             less
      4> data          hetrogenius      hetrogenius
      5> space         more             less
       

'''