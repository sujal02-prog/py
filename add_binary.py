try:
    a = input("Enter binary number: ")
    b = input("Enter abother binary: ")
    if a not in (0, 1):
        raise ValueError
    if b not in (0, 1):
        raise ValueError
except ValueError:
    print("Nah man, that's not binary, write again!")
