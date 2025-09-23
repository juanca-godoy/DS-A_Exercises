def make_change(a, b):
    bills = [20000, 10000, 5000, 2000, 1000]
    coins = [500, 100, 50, 25, 10, 5]

    change = b - a

    if a > b:
        raise ValueError("You do not have enough money to pay")
    elif change == 0:
        return "No change, you paid exact"
