class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_age(self):
        return self.age

def main():
    student1=student("sham",20)
    student2=student("andy",15)
    print(student1.age)
    del student1.age
   # print(student.age)
    print(student1.name)
    del student1.name

if __name__=="__main__":
    main()