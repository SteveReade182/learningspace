def myProgram():
    # create 3 functions for circle, triangle and rectangle areas
    import areas
    # from area import triangleArea, circleArea, rectangleArea
    again = "Yes"
    while again == "Yes":
        areas.welcome()
        print("Area finder! - Please choose the shape you would like find the area of?")
        userin = input("(T)riangle - (R)ectangle - (C)ircle (or X to exit): ").lower()
        if userin == "c":
            radius = int(input("Please input the radius of the circle: "))
            areas.circleArea(radius)

        elif userin == "r":
            length = int(input("Please input the height of the rectangle: "))
            width = int(input("Please input the width of the rectangle: "))
            areas.rectangleArea(length, width)

        elif userin == "t":
            height = int(input("Please input the height of the triangle: "))
            width = int(input("Please input the width of the triangle: "))
            areas.triangleArea(height, width)

        elif userin in "x":
            break
        else:
            print("Invalid Entry")

    print("Thankyou - Have a nice day")
    return




