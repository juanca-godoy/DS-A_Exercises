bills_coins = [20000, 10000, 5000, 2000, 1000, 500, 100, 50, 25, 10, 5]

charge_amount = 25000
pay_amount = 50000

change = pay_amount - charge_amount

for i in bills_coins:
    count = change // i
    if count > 0:
        change -= count * i
