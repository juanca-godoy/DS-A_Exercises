# P-Norm
import math


def norm(v, p=2):
    return sum([abs(x**p) for x in v]) ** (1 / p)


# --- Test Cases ---

# Test Case 1: Euclidean norm (default p=2)
print("norm([3, 4]) =", norm([3, 4]))
# Expected: 5.0

# Test Case 2: Manhattan norm (p=1)
print("norm([1, -2, 3], 1) =", norm([1, -2, 3], 1))
# Expected: 6

# Test Case 3: p=3 norm
print("norm([2, 2, 2], 3) =", norm([2, 2, 2], 3))
# Expected: ~2.884
