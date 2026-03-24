print("Conversion from Roman to Integer: ")
print("Here's a little table for ur easiness: ")
print("I   -   1")
print("V   -   5")
print("X   -   10")
print("L   -   50")
print("C   -   100")
print("D   -   500")
print("M   -   1000")

rom_num = input("Enter the Roman number: ")

sep_list = []
for i in rom_num.upper():
    sep_list.append(i)
print(sep_list)

b = len(sep_list) - 1

total = 0
prev = 0

for i in range(b,-1,-1):
    if sep_list[i] == "I":
        val = 1
    elif sep_list[i] == "V":
        val = 5
    elif sep_list[i] == "X":
        val = 10
    elif sep_list[i] == "L":
        val = 50
    elif sep_list[i] == "C":
        val = 100
    elif sep_list[i] == "D":
        val = 500
    elif sep_list[i] == "M":
        val = 1000

    if val < prev:
        total -= val
    else:
        total += val        
    
    prev = val

print("Integer value: ", total)
