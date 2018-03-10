# Υπολογιζμός παραγωντικού
def factorial(num):
    if num == 0:
        return 0
    else:
        return num*factorial(num-1)


print(factorial(int(input("Give me a number:"))))
