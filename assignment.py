# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:27:06 2023

@author: admin
"""
#Create a Animal class without any variables and methods
class animal:
    pass
#Create a Animal class with attributes sound(string), number_of_legs(integer) 
#and is_omnivore(boolean)
class animal1:
#Add a private attribute to the Animal class defined above named can_swim(boolean) 
#and define a getter and setter method for the same.
    def __init__(self,can_swim,number_of_legs, sound, is_omnivore):
        self.sound = sound
        self.is_omnivore = is_omnivore
        self.__number_of_legs = number_of_legs
        self.__can_swim = can_swim
        
    def get_can_swim(self):
        return self.__can_swim
    
    def set_can_swim(self, can_swim):
        if self.__number_of_legs<4:
            return "Cann't swim"
        else:
            self.__can_swim = can_swim
            return "Set successfully"

#Define a property for Animal class called hunts_for_food(boolean) 
#that must have the same value for every class instance (object) equalling true

class animal2:
    def __init__(self):
        self.hunts_for_food = True
anim = animal2()
print(anim.hunts_for_food)

#Modify the Animal class to count number of instances of the Animal class
#use com value 
class animal:
    count=0
    def __init__(self,sound):
        self.sound = sound
        animal.count=animal.count+1
anim1 = animal("Bark")
anim2 =animal("laughing")
anim3 =animal("shouting")
anim4 =animal("screeming")
print(anim1.count)
#Create a list of Animal objects(minimum 5) and then iterate through them and 
#print their attributes
list1 =[anim1, anim2, anim3, anim4]
for i in list1:
    print(i.sound)