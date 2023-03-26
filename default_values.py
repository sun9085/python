class student:
    def __init__(self,name,age=25):
         self.name=name
         self.age=age

    def print_student_details(self):
        print("printing student details:",self.name,self.age)

def main():
    student1=student("ram")
    student1.print_student_details()

if __name__=="__main__":
    main()