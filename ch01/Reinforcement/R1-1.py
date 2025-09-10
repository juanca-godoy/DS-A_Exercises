# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
# ----------------------------------------------------------------------------------
# Do a MODULO operation. If no remainder then it is a multiple
# If there is a remainder it is not a multiple thus false
def is_multiple(n, m):
    return n % m == 0


print(is_multiple(6, 2))
