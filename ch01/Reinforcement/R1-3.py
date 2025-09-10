# Check in a loop for every value the smallest and largest
def minmax(data):
    min = max = data[0]
    for val in data:
        if val < min:
            min = val
        elif val > max:
            max = val
    return (min, max), vars()


data = [1, 2, 3, 12, 4, -2, 6, 8, -304, 5, 500]

print(minmax(data))
