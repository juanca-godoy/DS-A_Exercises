# Do a bitwise operation using & (AND)
# Compares binary 1 with the binary k and if last bit is 0 then EVEN otherwise ODD
def is_even(k):
    return k & 1 == 0


print(is_even(11))
