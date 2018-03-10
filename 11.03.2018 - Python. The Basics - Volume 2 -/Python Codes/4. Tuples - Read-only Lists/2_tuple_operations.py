my_tuple = (1, 2, 3)
str_tuple = ('hello!',)

print("Tuple Length:", len(my_tuple))
print("Concatenation with (3, 4):", my_tuple + (3, 4))
print("Multiplication:", str_tuple*2)
print("Search. Is 2 in my_tuple?", 2 in my_tuple)

print("Values in my_tuple:")
for x in my_tuple:
    print(x)