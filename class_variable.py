class Student:
    school_name="saraswati vidya mandir"
    def __init__(self,name,age):
        self.name=name
        self.age=age

def main():
    stu1=Student("pratik",17)
    stu2=Student("ram",14)
    print(stu1.name,stu1.age)
    print(stu2.name,stu2.age)
    print(stu1.school_name,stu2.school_name,Student.school_name)

if __name__=="__main__":
    main()