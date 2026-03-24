while True:
    a = input("Enter string/text/word of ur liking: ")
    if a.isalpha():
        break
    else:
        print("Nah man! that's not string. Try again. ")

print("So, ur string is this: ",a)

b = []

for i in a:
    if i in b:
        break
    b.append(i)
    
print("The max num of letter neighbors without repeating is: ", len(b))
