x = int(input("Give a number: "))

if x < 10:

    if x < 5:
        print("x is less than 5")
    else:
        print("x is greater than 5 and less than 10")

elif x >= 10 and x < 20: #Can be written as x <= 10 < 20

    if x < 15:
        print("x is less than 15 and greater or equal than 10")
    elif x == 15:
        print("x is 15")
    else:
        print("x is greater than 15 and less than 20")
else:
    print("x is greater than 20 or equal")
