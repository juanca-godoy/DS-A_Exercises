# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.


def catdog(prefix, remaining):
    """Recursive function for finding all combinations of string 'catdog'

    Args:
        prefix (string): The letters we have used in combination
        remaining (string): The remaining letters of the string 'catdog' not used yet
    """
    if not remaining:
        print(prefix)
        return
    for i in range(len(remaining)):
        new_prefix = prefix + remaining[i]
        new_remaining = remaining[:i] + remaining[i + 1 :]
        catdog(new_prefix, new_remaining)


chars = "catdog"
catdog("", chars)
