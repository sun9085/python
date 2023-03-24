class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self):
        self.name = "Random Name"


def main():
    student = Student()
    print("Object created")


if __name__ == "__main__":
    main()
