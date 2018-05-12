# Έχουμε διάφορους τρόπους να κάνουμε print "πολλές γραμμές μηνυμάτων"

# 1ος Τρόπος ( Συνιθισμένος για αρχάριους )
print("==== Welcome to your first menu ====")
print("1) Add item to list")
print("2) Delete number from list")
print("3) Print list")
print("4) Maximum number in list")
print("5) Minimum number in list")
print("0) Quit")

# 2ο Τρόπος ( Συνιθισμένος, με μία εντολή print, αλλά ΑΣΧΗΜΟΣ )
print("==== Welcome to your first menu ==== \
      \n1) Add item to list \
      \n2) Delete number from list \
      \n3) Print list \
      \n4) Maximum number in list \
      \n5) Minimum number in list \
      \n0) Quit \
        ")

# 3ος Τρόπος ( Μια εντολή print, αλλά κρατάει τα κενά.. καμιά φορά δεν το θέλουμε.. )
print("""
==== Welcome to your first menu ====
1) Add item to list
  2) Delete number from list
3) Print list
      4) Maximum number in list
    5) Minimum number in list
0) Quit
""")

# 4ος Τρόπος ( Προτίμητέος, μία εντολή print, καθαρός κώδικας)
print(
    '==== Welcome to your first menu ====\n'
    '1) Add item to list\n'
    '2) Delete number from list\n'
    '3) Print list\n'
    '4) Maximum number in list\n'
    '5) Minimum number in list\n'
    '0) Quit\n'
)
