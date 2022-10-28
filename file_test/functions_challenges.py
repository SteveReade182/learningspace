# create 3 functions for circle, triangle and rectangle areas
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
again = "Yes"
while again == "Yes":
    print("Area finder! - Please choose the shape you would like find the area of?")
    userin = input("(T)riangle - (R)ectangle - (C)ircle (or X to exit): ").lower()
    if userin == "c":
        radius = int(input("Please input the radius of the circle: "))
        circleArea(radius)

    elif userin == "r":
        length = int(input("Please input the height of the rectangle: "))
        width = int(input("Please input the width of the rectangle: "))
        rectangleArea(length, width)

    elif userin == "t":
        height = int(input("Please input the height of the triangle: "))
        width = int(input("Please input the width of the triangle: "))
        triangleArea(height, width)

    elif userin in "x":
        break
    else:
        print("Invalid Entry")

print("Thankyou")



