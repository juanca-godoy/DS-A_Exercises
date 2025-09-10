# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.
def reverse_list(data):
    """Reverse a list on integers.

    This function takes a list of integers and returns a new list with
    the elements in reverse order

    Args:
        data (list[obj]): A list of objects

    Returns:
        list[obj]: A new list with the elements reversed.
    """
    n = len(data)  # Get the length of the list
    for i in range(
        n // 2
    ):  # Iterate the floor half of the list. i.e. len = 5, the just need to iterate 2
        # Swap operation. Switch the element in front data[i] with element in back data[n - 1 - i]
        data[i], data[n - 1 - i] = data[n - 1 - i], data[i]
    return data


data = [1, 2, 3, 4, 5]
print("String reverse with function", reverse_list(data))
