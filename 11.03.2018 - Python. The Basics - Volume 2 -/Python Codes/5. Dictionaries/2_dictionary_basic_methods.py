myDict = {
    'Name': 'John',
    'Surname': 'Ioannou',
    'Age': 20,
    'Birth Date': '2/11/1998'
}

# Νέο dictionary με μία τιμή
dictTemp = {'Semester': 4}

# Κλήση της συνάρτησης update
myDict.update(dictTemp)

print(myDict)

# Διαγραφή του στοιχείου 'Birth Date'
del myDict['Birth Date']

print(myDict)

# Εύρεση μεγέθους του Dictionary
print("Current Dictionary Length:", len(myDict))

# Εκκαθάριση του Dictionary
myDict.clear()

print(myDict)

# Διαγραφή του Dictionary
del myDict

# Άμα κάνω print τώρα θα μου πετάξει error... Ξέρεις γιατί;
# Δοκίμασε το!
# print(myDict)