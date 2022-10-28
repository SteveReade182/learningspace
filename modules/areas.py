import math

def circleArea(radius):
    area = radius * radius * math.pi
    print(area)
    return area

def triangleArea(height,width):
    area = height * width /2
    print(area)
    return area

def rectangleArea(length,width):
    area = length * width
    print(area)
    return area

def welcome():
    print(
        """
        -This is a program-
        -------------------
        -------enjoy-------
        -------------------
        ------Steve R------
        -------------------
        """
    )
    return