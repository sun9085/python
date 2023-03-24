class Student:  # Constructor with default values

    def __init__(self, name, age=17):
        self.age = age
        self.name = name

    def print_student_details(self):
        print("This is for the student details ", self.name, self.age)


def main():
    student = Student("Ram")
    student.print_student_details()


if __name__ == "__main__":
    main()
