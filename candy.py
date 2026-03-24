def candies(num1):
    count = a
    for i in range((a-1)):
        if num1[i] == num1[i+1]:
            continue
        elif num1[i] > num1[i+1]:
            continue
        else:
            count += 1
    return count

num1 = []
a = int(input("enter the number of children: "))
for i in range(a):
    x = int(input(f"enter rating {i+1}: "))
    num1.append(x)
print(num1)
print("The minimun number of candies u need is: ", candies(num1))
