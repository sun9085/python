class Animal:
    def __init__(self,name,species,nikname):
        self.name=name
        self._species=species
        self.nikname=nikname

    def get_species(self):
        return self._species

class Dog(Animal):
    def __init__(self, name, species,nikname):
        super(Dog,self).__init__(name,species,nikname)

    def get_dog_nikname(self):
        return self.nikname

def main():
    animal=Animal("tomy","labrador","chotu")
    print(animal._species,animal.name)
    dog=Dog("jony","lan","mima")
    print(dog.name,dog._species)


if __name__=="__main__":
    main()

