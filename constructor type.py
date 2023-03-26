print(" type_1: constructor with pass statement")

class student:
    pass

def main():
    s=student()
    print("  created object sucessfully")

if __name__ == '__main__':
    main()

print("*"*100)


print(" type_2: constructor with : arguments")

class student:

    def __init__(self,name,age):
        self.age=age
        self.name=name


def main():
    s=student("sam",25)
    print("age of sam is :",s.age)
    print("and name is:",s.name)

if __name__ == '__main__':
    main()

print("*"*100)

print("type_3: constructor sigle method ")

class student:

    def method(self):
        print("i am in student class method")

def main():
    s=student()
    print(s)

if __name__ == '__main__':
    main()

print("*"*100)

print("type_4 : constructor with default values")

class student:

    def __init__(self,name,age=20,r_no=30):    # default values set age=20 ,     r_no=30

        self.name=name
        self.age=age
        self.r_no=r_no



    def show_details(self):
        return (self.name,self.age,self.r_no)

def main():

    student1=student("santosh")
    print("name is:",student1.name)
    print("age is:",student1.age)
    print("r_no:",student1.r_no)

    print("this is method use to print all details of student")
    print(student1.show_details())


if __name__ == '__main__':
    main()