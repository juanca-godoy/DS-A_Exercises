# Use range to return all numbers starting from 1 and until n - 1
# Use the assign iperator += and i * i in the loop
# Return the total
# Step by 2 in the range
def sum_squares(n):
    total = 0
    for i in range(1, n, 2):
        total += i * i
    return total


print(sum_squares(5))
