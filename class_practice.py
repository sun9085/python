class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(self.name,"barking ")
    def eat(self):
        print(self.name,"eating chiken")

s=animal("roksy",5)
print(s.name,s.age)
s.bark()
s.eat()