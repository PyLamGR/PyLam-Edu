import os
os.chdir("C:\\Users\\Taxiarchis\\Desktop\\Files_python")
with open("write.txt","wb") as file:
    a_list = ["This is " ," how "," we ","\n","write " ,"to ","files"]
    for word in a_list:
        file.write(word)

