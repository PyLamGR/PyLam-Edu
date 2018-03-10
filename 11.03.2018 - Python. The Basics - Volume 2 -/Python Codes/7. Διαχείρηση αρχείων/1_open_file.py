import os
os.chdir("C:\\Users\\Taxiarchis\\Desktop\\Files_python")  # Αλλάξτε το αυτό ανάλογα το PATH
file = open("text.txt","r")
print(file.readline())
file.close()

