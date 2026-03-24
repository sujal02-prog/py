alist = []

a = int(input("Enter the number of elements of array: "))
for i in range(a):
    x = int(input(f"Enter number {i+1}: "))
    alist.append(x)

b = int(input("Enter the number of different integer u want in ur subarrays: "))
if b > a:
    raise Exception("The subarray cant be greater than main array, u dumbass!")

blist = []

for i in range(a):
    for j in range(i,a):
        blist.append(alist[i:j+1])
    
c = len(blist)

for i in range(c):
    if b <= len(blist[i]):
        print(blist[i])
        print("lol")
        







