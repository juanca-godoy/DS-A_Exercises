# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.
def odd_product(data):
    odd_values = {x for x in data if x % 2 == 1}
    return len(odd_values) > 1


data = [1, 2, 3, 4, 5, 5]
print(odd_product(data))
