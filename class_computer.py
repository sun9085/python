class computer:

    computer="dekstop / pc"

    def __init__(self,brand,year,graphic_card,ram,ssd,prosessor,generation):
        self.brand=brand
        self.year=year
        self.graphic_card=graphic_card
        self.ram=ram
        self.ssd=ssd
        self.prosessor=prosessor
        self.generation=generation


    def get_year(self):
        return self.year
    def set_year(self,year):
        self.year=year


omega=computer("intel","2023","AMDS","4GB","250_GB","2.4ghz","i7")
print("brand of cmputer is:",omega.brand)
print("year of manufacturing computer is:",omega.year)
print("ghraphic_card of computer is:",omega.graphic_card)
print("RAM of computer is:",omega.ram)
print("ssd of computer is:",omega.ssd)
print("prosessor of computer is:",omega.prosessor)
print("generation of computer is :",omega.generation)

print("get_year method:",omega.get_year())
print("set_year method set new yaer:",omega.set_year(2025))
print("we set new year:",omega.get_year())