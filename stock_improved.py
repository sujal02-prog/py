def stock_find(stock):

    min_price = stock[0]
    max_profit = 0

    for price in stock:

        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


stock = []

a = int(input("Enter the number of total stocks: "))

for i in range(a):
    x = int(input(f"Enter stock {i+1}: "))
    stock.append(x)

print(stock)

print("The max profit is:", stock_find(stock))
