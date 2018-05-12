my_dict = {
    'Name': 'John',
    'Surname': 'Ioannou',
    'Age': 20,
    'Birth Date': '2/11/1998'
}

print(my_dict)

print("Get key 'Name':", my_dict.get('Name'))
print("Print Values:", list(my_dict.values()))
print("Print Keys:", list(my_dict.keys()))
print("Print as Items:", list(my_dict.items()))
