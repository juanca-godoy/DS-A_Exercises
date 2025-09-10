# Use range and step by 2 starting on 1 to get odd numbers
def sum_oddsquares(n):
    return sum(i * i for i in range(1, n, 2))


print(sum_oddsquares(10))
