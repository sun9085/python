class student:   # default constructor

    def print_student_details(self):
        print("this is the students details")



class student_example1:         ## default constructor no arguments

    def __init__(self):
        pass

    def print_student_details(self):
        print("this is the students details")


class student_example2:   ## constructor with arguments


    def __init__(self,age,name):
        self.age=age
        self.name=name


    def print_students_deatils(self):
        print("this is the students details",self.age,self.name)

def main():
    student0=student()
    student1=student_example1()
    student2=student_example2("sunny",12)
    student0.print_student_details()
    student1.print_student_details()
    student2.print_students_deatils()

if __name__=="__main__":
    main()