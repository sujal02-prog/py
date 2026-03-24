a = int(input("Enter any number greater than zero: "))

if a < 0:
    raise Exception("Number greathan than zero, dumbass!")

list1 = []

for i in str(a):
    list1.append(int(i))
print(list1)

b = len(list1)

num = None
list2 = []

while True:
    num = list1[0]*list1[0]+list1[1]*list1[1]
    if num in list2:
        print("It is not a happy number.")
        break
    list2.append(num)
    if num == 1:
        print("It is a happy number.")
        break
    else:
        list1.clear()
        for i in str(num):
            list1.append(int(i))
        
