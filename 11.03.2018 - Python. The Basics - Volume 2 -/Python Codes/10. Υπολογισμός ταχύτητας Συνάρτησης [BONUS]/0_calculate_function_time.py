import timeit


# Υλοποίηση μίας συνάρτησης
def func():
    for i in range(1000):
        print(i)


# Υλοποίηση εντολής για μέτρηση του χρόνου εκτέλεσης
# της συνάρτησης func για 1 μόνο φορά
# και αποθήκευση του χρόνου σε μία μεταβλητή
final_time = timeit.timeit(func, number=1)

print("Time elapsed for function func is:", final_time)