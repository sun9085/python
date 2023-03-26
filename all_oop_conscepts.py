# create class

class student:                                             # class name : student
    school_name="new marathi medium school"                # global varibale
    def __init__(self,name,age,roll_no,div):
        self.name=name                                     # local variable of class student
        self.age=age
        self.roll_no=roll_no
        self.div=div

student_first=student("suraj",14,22,"A")                    # 1 st object of class
student_second=student("samiksha",13,12,"B")                 # 2nd object of class
student_third=student("vikram",11,23,"C")                       # 3rd object of class

print("printing all names of students:",student_first.name,student_second.name,student_third.name)
print("printing all ages of students:",student_first.age,student_second.age,student_third.age)
print("printing all roll_no of students:",student_first.roll_no,student_second.roll_no,student_third.roll_no)
print("printing all division of students:",student_first.div,student_second.div,student_third.div)

print("*"*100)

##      crate constructor of class

class Student:
    def __init__(self):                 # constructor of class
        pass                            # pass means jump statement in python

def main():                             # create main function
    new_obj=Student()                   # create new object
    print("object is created")          # print meassge here

if __name__=="__main__":               # this satetement use for futre
    main()                             # complete function

print("*"*100)

##      class varibles

class  student:

    school_name="om shanti primary school"              # class variable like global

    def __init__(self,name,age,div):                   # class variable : name,age,div
        self.name=name
        self.age=age
        self.div=div                                    ## instance variable: NAME,AGE,DIV

def main():
    student1=student("sagar",10,"A")                                        # object 1
    student2=student("atharva",12,"D")                                      # object 2
    print("name:",student1.name,"age:",student1.age,"div:",student1.div)
    print("name:",student2.name,"age:",student2.age,"div:",student2.div)
    print(student1.school_name,",",student2.school_name)
if __name__=="__main__":
    main()
print("*"*100)                 # over code /end code