# Using list comprehension:
# i * i = is the square part, and what is getting added
# i -> the iterator
# range(1, n) the range from 1 to n-1
n = 6
total = sum(i * i for i in range(1, n))

print(total)
