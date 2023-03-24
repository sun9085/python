
import sys


class Point2D:
    def __init__(self, x: float, y: float):
        """
        Point2D constructor
        :param x: x coordinate of a point
        :param y: y coordinate of a pont
        """
        self.x = x
        self.y = y


class Triangle:

    def __init__(self, ptA: tuple, ptB: tuple, ptC: tuple):
        """
        Constructor of triangle
        :param ptA: tuple: x, y coordinates of vertex A
        :param ptB: tuple: x, y coordinates of vertex B
        :param ptC: tuple: x, y coordinates of vertex C
        """
        # step 1: Calculate the lengths of sides
        len_AB = ((ptA[0] - ptB[0]) ** 2 + (ptA[1] - ptB[1]) ** 2) ** 0.5
        len_BC = ((ptB[0] - ptC[0]) ** 2 + (ptB[1] - ptC[1]) ** 2) ** 0.5
        len_CA = ((ptC[0] - ptA[0]) ** 2 + (ptC[1] - ptA[1]) ** 2) ** 0.5

        # Step 2: Check for error
        if( (len_AB + len_BC <= len_CA) or
            (len_BC + len_CA <= len_AB) or
            (len_AB + len_CA <= len_BC)
           ):
            print("Summation of two sides of a triangle is not greater than the third!")
            sys.exit(-1)

        self.vA = Point2D(ptA[0], ptA[1])
        self.vB = Point2D(ptB[0], ptB[1])
        self.vC = Point2D(ptC[0], ptC[1])

        self.AB = len_AB
        self.BC = len_BC
        self.CA = len_CA

    def getAB(self) -> float:
        """
        :return: length of side AB
        """
        return self.AB

    def getBC(self) -> float:
        """
        :return: length of side BC
        """
        return self.BC

    def getCA(self) -> float:
        """
        :return: length of side CA
        """
        return self.CA

T = Triangle((-3.5, 1.5), (1.0, 4.0), (4.5, 1.5))
print(T.__dict__)
print(T.__dict__['vA'].__dict__)
print(T.__dict__['vB'].__dict__)
print(T.__dict__['vC'].__dict__)

