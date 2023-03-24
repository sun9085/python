class Student:
    school_name = "Random School"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_student_information(self):
        print("Student name is: ", self.__name, " and age is: ", self.__age)


def main():
    student = Student("Ram", 17)
    student.show_student_information()


if __name__ == "__main__":
    main()
