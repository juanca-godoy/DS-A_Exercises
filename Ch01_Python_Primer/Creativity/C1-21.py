# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).


def reverse():
    data = []
    while True:
        try:
            user_in = input("Please enter a line: ")
            data.append(user_in)
        except EOFError:
            print("You have reached the end of the file")
            return data[::-1]


print(reverse())
