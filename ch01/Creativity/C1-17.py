# C-1.17 Had we implemented the scale function (page 25) as follows, does it work
# properly? Explain why or why not.

# It would not work, because it is only updating the local variable 'val', not the
# list object itself. Because numeric typer are immutable, the scale would only
# create a new number object, but is never written back into the list.
# As a result, the caller's list remains unchanged.
def scale(data, factor):
    for val in data:
        val *= factor
