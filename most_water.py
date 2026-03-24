height = []
a = int(input("Enter the number of vertical lines: "))
for i in range(a):
    x = int(input(f"Enter number {i+1}: "))
    height.append(x)

mul1 = 0

for i in range(a):
    for j in range(1,a):
        mul = min(height[i],height[j]) * (j-i)
        if mul > mul1:
            mul1 = mul

print("The max amount of water that can be stored is: ", mul1)
