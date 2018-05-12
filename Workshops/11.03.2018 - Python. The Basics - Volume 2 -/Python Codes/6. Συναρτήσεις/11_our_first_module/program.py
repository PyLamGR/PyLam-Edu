from . import name_check as n

name = input("What's your name?\n")
n.print_capitals(name)
n.print_smalls(name)

nums = n.name_letters(name)
print(nums)

nums = n.count_capitals(name)
print(nums)

nums = n.count_lowercasse(name)
print(nums)
print(n.c)
