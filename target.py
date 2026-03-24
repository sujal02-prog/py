def indices(num):
    for i in range(len(num)):
        for j in range(len(num)):
            if b == num[i]+num[j] and i != 0:
                return i,j

num = []
a = int(input("Enter the number of elements in ur array: "))
for i in range(a):
    x = int(input(f"Enter number {i+1}: "))
    num.append(x)
b = int(input("Enter the target number: "))
num.sort()
print(num)
print("Target: ",b)
index = list(indices(num))
print("The indices that will give the target is: ", index)
