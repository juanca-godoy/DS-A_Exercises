# C-1.16 In our implementation of the scale function (page 25), the body of the loop
# executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?

# A: The list is mutable. So you break the alias for the numbers
# but assign new number objects at the position J (scaled) of the list which IS mutable.
# Since the data refers to the caller's list, the caller sees the updates.


def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
