class animal:

    def __init__(self,type,name,age):
        self.type=type
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name

    def set_age(self,age):
        return  set.__age =age