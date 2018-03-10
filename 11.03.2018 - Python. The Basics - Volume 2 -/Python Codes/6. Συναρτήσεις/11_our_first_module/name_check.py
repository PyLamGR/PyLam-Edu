def print_capitals(name):
    print(name.upper())


def print_smalls(name):
    print(name.lower())


def name_letters(name):
    return list(name)


def count_capitals(name):
    cnt = 0
    for i in name:
        if i.isupper():
            cnt += 1
    return cnt


def count_lowercasse(name):
    cnt = 0
    for i in name:
        if i.islower():
            cnt += 1
    return cnt


c = 10.4