def median1():
    if c % 2 != 0:
        return num3[d]
    else:
        return e

num1 = []
a = int(input("enter the number of element u want to put in array1: "))
for i in range(a):
    x = int(input(f"enter number {i+1}: "))
    num1.append(x)
num1.sort()
print(num1)
num2 = []
b = int(input("enter the number of element u want to put in array2: "))
for i in range(b):
    y = int(input(f"enter number {i+1}: "))
    num2.append(y)
num2.sort()
print(num2)
num3 = num1 + num2
num3.sort()
c = a + b
d = int((c/2)-0.5)
e = ((num3[c//2]+num3[(c//2)-1])/2)
print(num3)
print("The median of the combined array is: ", median1())
