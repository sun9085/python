class animal:

    def __init__(self,sound:str,no_leg:int,omnivorce):
        self.sound=sound
        self.no_leg=no_leg
        self.omnivorce=omnivorce


def main():
    dog=animal("barking",4,True)
    print(dog.sound)
    print(dog.no_leg)
    print(dog.omnivorce)

if __name__=="__main__":
    main()
