def divide2(n):
    count = 0
    while n > 2:
        n = n / 2
        count += 1
    return count


n = int(input("Please enter a positive integer: "))
print(divide2(n))
