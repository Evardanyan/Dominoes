def quadrant(x, y):
    if x > 0 and y > 0:
        print("I")

    elif x < 0 < y:
        print("II")

    elif x < 0 and y < 0:
        print("III")

    elif x > 0 > y:
        print("IV")

    # elif (x == 0 and y > 0):
    #     print("lies at positive y axis")
    #
    # elif (x == 0 and y < 0):
    #     print("lies at negative y axis")
    #
    # elif (y == 0 and x < 0):
    #     print("lies at negative x axis")
    #
    # elif (y == 0 and x > 0):
    #     print("lies at positive x axis")
    #
    # else:
    #     print("lies at origin")


num1 = float(input())
num2 = float(input())
quadrant(num1, num2)