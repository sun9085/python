class Student:
    school_name = "Saraswati Vidya Mandir"

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.__marks = marks


def main():
    student1 = Student("Ram", 17, 100)
    print(student1.age)
    # print(student1.__marks)
    print(student1._Student__marks)


if __name__ == "__main__":
    main()
