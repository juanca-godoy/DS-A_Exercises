# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.


def count_vowels(n):
    vowels = {"a", "e", "i", "o", "u"}
    return sum(1 for char in n.lower() if char in vowels)


print(count_vowels("Hello"))
