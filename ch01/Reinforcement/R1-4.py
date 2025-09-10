# Use range to return all numbers starting from 1 and until n - 1
# Use the assign iperator += and i * i in the loop
# Return the total
def sum_squares(n):
    total = 0
    for i in range(1, n):
        total += i * i
    return total


print(sum_squares(5))
