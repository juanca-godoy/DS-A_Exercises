# C-1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”


def arithmetic():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    if a + b == c:
        print(f"{a} + {b} = {c}")
    elif b - c == a:
        print(f"{b} - {c} = {a}")
    elif a * b == c:
        print(f"{a} * {b} = {c}")
    else:
        print("No valid arithmetic formula")


arithmetic()
