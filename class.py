class student:
    school="nutan vidyalya"                                            """ global variable of class"""

    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
student_1=student("amit",12,165.2,50)
print(student_1.name,student_1.age,student_1.height,student_1.weight)
print(student_1.school)



student2=student("govind",14,160.1,47)
print(student2.name,student2.age,student2.height,student2.weight)
print("*"*50)

class car:
    car_rto="maharashtra_RTO"
    def __init__(self,brand,price,model,passing):
        self.brand=brand
        self.price=price
        self.model=model
        self.passing=passing

    def get_brand(self):
        return self.brand

    def get_price(self):
        return self.price

    def set_brand(self,brand):
        self.brand=brand

    def set_price(self,price):
        self.price=price

car1=car("landrover",7500000,"discovry_sport","mh14")
print(car1.brand,car1.price,car1.model,car1.passing)
car2=car("mahinndra",2000000,"xuv700","mh12")
print(car2.brand,car2.price,car2.model,car2.passing)
print(car1.car_rto)
print(car2.get_price())
print(car2.set_price(1000000))
print(car2.get_price())
