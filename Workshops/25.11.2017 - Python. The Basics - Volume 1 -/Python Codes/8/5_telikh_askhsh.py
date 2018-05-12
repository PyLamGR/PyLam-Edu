# Η εργασία που είχε μπεί στο τέλος, για το πρώτο τμήμα

my_list = []

# Λίστα με στοιχεία από το 1 μέχρι το 25

for i in range(25):
    my_list.append(i)

# Αφαίρεση ζυγών αριθμών

for i in range(25):
    if i % 2 == 0:
        my_list.remove(i)

print(my_list)
