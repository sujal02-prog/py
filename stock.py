def stock_find(stock):
    ss = 0
    b = 1 
    ss = stock[0]

    for i in range(len(stock)):
        if ss > stock[i]:
            ss = stock[i]
            b = i + 1

    bs = 0
    c = 1
    bs = stock[b-1]

    for j in range((b-1), len(stock)):
        if bs < stock[j]:
            bs = stock[j]
            c = j + 1

    return b, c, bs - ss

stock = []

a = int(input("Enter the number of total stocks: "))
for i in range(a):
    x = int(input(f"Enter stock {i+1}: "))
    stock.append(x)
    
print(stock)
b, c, stock_123 = stock_find(stock)
print("The time when u should buy stock is day:", b)
print("The time when u should sell stock is day:", c)
print("The max profit is: ",stock_123)
