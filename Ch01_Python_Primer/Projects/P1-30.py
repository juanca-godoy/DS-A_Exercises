def half(n):
    """Recursively go through N and find the number of times it needs to be
    divided by 2 before being less than 2

    Args:
        n (int): a positive integer larger than 2

    Returns:
        int: a count of the numbers of times n was divided by 2 before being less than 2
    """
    if n < 2:
        return 0
    else:
        return 1 + half(n / 2)


n = int(input("Please enter a positive integer: "))
print("Number of divisions: ", half(n))
