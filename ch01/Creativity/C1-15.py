# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).
def distinct(data):
    return len(data) == len(set(data))


def distinct2(data):
    """Check if all items in a list are distinct.

    Args:
        data (list(obj)): It takes a list of objects

    Returns:
        Boolean: It returns True if all items are distinct.
        False if there is at least 1 duplicate
    """
    seen = []
    for x in data:
        if x in seen:
            return False
        else:
            seen.append(x)
    return True


data = [1, 2, 3, 2]
print(distinct2(data))
