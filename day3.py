# diigferent class diffrent methoids  no type cheikng  into tuple
class vehicle:
    def __init_(self,color,make):
        self.color=color
        self.make=make

    def get_color(self):
        return self.color
    def get_make(self):
        return self.make


class car:
    def __init_(self, color, make):
        self.color = color
        self.make = make

    def get_color(self):
        return self.color

    def get_make(self):
        return self.make


def main():
     v1=vehicle("balck","bmw")
     c1=car("white","suzuki")
     for object in (vehicle,car):
         print(object.get_make(),object.get_color())

if __name__=="__main__":
    main()

