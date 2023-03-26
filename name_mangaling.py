class student:
    school_name="prashala"
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.__marks=marks

def main():
    student1=student("amit",11,100)
    print(student1.age)
    print(student1._student__marks)


if __name__=="__main__":
    main()
