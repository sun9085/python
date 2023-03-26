class vehicle:
    def __init_(self,color,make):
        self.color=color
        self.make=make

    def get_color(self):
        return self.color
    def get_make(self):
        return self.make

def print_values(obj):
    print(obj.get_make(),obj.get_make)


def main():
    vehicle = vehicle("balck", "bmw")
    car = car("white", "suzuki")
   print_values(vehicle)
   print_values(car)


if __name__ == "__main__":
    main()
