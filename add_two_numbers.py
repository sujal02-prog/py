list1 = []
list2 = []

a = int(input("Enter the number of elements u want in ur list1: "))
for i in range(a):
    x = (input(f"Enter number {i+1}: "))
    list1.append(x)

b = int(input("Enter the number of elements u want in ur list2: "))
for i in range(b):
    y = (input(f"Enter number {i+1}: "))
    list2.append(y)

print("First list: ",list1)
print("Second List: ",list2)

num1 = str(0)
for i in range((len(list1)-1),-1,-1):
    num1 += list1[i]

num2 = str(0)
for i in range((len(list2)-1),-1,-1):
    num2 += list2[i]

print(num1, num2)

add = int(num1) + int(num2)
print(add)

new_list = []
#for i in range(len(add)-1,-1,-1):
for i in reversed(str(add)):
    new_list.append(i)

print(new_list)
