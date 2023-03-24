

class Date:

    def __init__(self, init_day: int, init_month: int, init_year: int):
        self.day = init_day
        self.month = init_month
        self.year = init_year


    def get_day(self) -> int:
        """
        :return: returns the day component
        """
        return self.day

    def set_day(self, new_day: int) -> None:
        """
        Sets the day component to given value
        :param new_day: int: new day value
        :return: None
        """
        self.day = new_day

    def get_month(self) -> int:
        """
        :return: returns the month component
        """
        return self.month

    def set_month(self, new_month: int) -> None:
        """
        Sets the month component to a given value
        :param new_month: int: new month value
        :return: None
        """
        self.month = new_month

    def get_year(self) -> int:
        """
        :return: Year component of a Date object
        """
        return self.year

    def set_year(self, new_year: int) -> None:
        """
        Sets the year component to a given value
        :param new_year: new year valye
        :return: None
        """
        self.year = new_year


D = Date(19, 10, 2021)

dd = D.get_day()
print("Day:", dd)
D.set_day(25)
dd = D.get_day()
print("Modified day:", dd)

mm = D.get_month()
print("Month:", mm)
D.set_month(4)
mm = D.get_month()
print("Modified month:", mm)

yy = D.get_year()
print("Year:", yy)
D.set_year(2025)
yy = D.get_year()
print("Modified year:", yy)
