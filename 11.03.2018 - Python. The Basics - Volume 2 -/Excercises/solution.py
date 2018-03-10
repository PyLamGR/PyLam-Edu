def print_list():
    if not my_list:
        print("The list is empty!")
    else:
        print(my_list)


def main():
    my_list = []

    # Δημιουργώ έναν ατέρμονα βρόγχο
    while True:
        print(
            '==== Welcome to your first menu ====\n'
            '1) Add item to list\n'
            '2) Delete number from list\n'
            '3) Print list\n'
            '4) Maximum number in list\n'
            '5) Minimum number in list\n'
            '6) Sort Ascending\n'
            '7) Sort Descending\n'
            '0) Quit\n'
        )

        choice = int(input("What do you want to do this time? : "))

        if choice == 1:  # Εισαγωγή στοιχείου στην λίστα
            num = int(input("What's the number you want to add? : "))
            my_list.append(num)
        elif choice == 2:  # Διαγραφή στοιχείου απο την λίστα
            num = int(input("What's the number you want to delete? : "))
            my_list.remove(num)

            # Ερώτηση... Πως βγάζουμε μήνυμα λάθους αν το στοιχείο δεν είναι μέσα;
        elif choice == 3:  # Εκτύπωση λίστας
            print_list()
        elif choice == 4:  # Εύρεση μεγίστου
            result = max(my_list)  # Αποθήκευση της μέγιστης τιμής της λίστας στην μεταβλητή "result"
            print("The biggest number is: ", result)
        elif choice == 5:  # Εύρεση ελαχίστου
            print("The smallest number is: ", min(my_list))
        elif list == 6:  # Ταξινόμηση αύξουσα
            my_list.sort()
            print_list()
        elif list == 7:
            my_list.sort(reverse=True)
            print_list()
        elif choice == 0:  # Έξοδος προγράμματος
            print("Good bye, see you soon!")
            break
        else:  # Διαχείρηση λάθος τιμών μενού..
            print("You had 4 choices how can you mess up ... try again!")

    print("The program has exited")  # Βοηθητικό μήνυμα για να δείξουμε οτι βγήκαμε απο τον ατέρμονα βρόγχο


if __name__ == "__main__":
    main()
