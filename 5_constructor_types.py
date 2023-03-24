class Student:  # Default Constructor provided by Python

    def print_student_details(self):
        print("This is for the student details in Example 0")


class StudentExample1:  # Constructor with no arguments

    def __init__(self):
        pass

    def print_student_details(self):
        print("This is for the student details in Example 1.")


class StudentExample2:  # Constructor with arguments

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_student_details(self):
        print("This is for the student details in Example 2", self.age, self.name)


def main():
    student0 = Student()
    student1 = StudentExample1()
    student2 = StudentExample2("Ram", 17)
    student0.print_student_details()
    student1.print_student_details()
    student2.print_student_details()


if __name__ == "__main__":
    main()
