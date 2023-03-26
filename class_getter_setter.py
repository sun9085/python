class  Student:

    def __init__(self,name,age,marks):
        self.name=name
        self.__age=age
        self.__marks=marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if self.__age <17 :
            return "not allow"
        else:
            self.__marks=marks
            return "marks add sucsessfully"

def main():
    stu1=Student("avinash",14,100)
    print(stu1.get_marks())
    print(stu1.set_marks(90))
    print(stu1.get_marks())

if __name__=="__main__":
    main()