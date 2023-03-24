class Animal:
    def __init__(self, name, species, nickname):
        self.name = name
        self._species = species
        self.__nickname = nickname

    def get_species(self):
        return self._species


class Dog(Animal):
    def __init__(self, name, species, nickname):
        super(Dog, self).__init__(name, species, nickname)

    def get_dog_nickname(self):
        return self.__nickname


def main():
    animal = Animal("Caesar", "Cat", "Cassie")
    print(animal._species, animal.name)
    dog = Dog("Caeser", "Dog", "Kaizer")
    # print(dog.get_dog_nickname())
    print(dog.get_species())


if __name__ == "__main__":
    main()
