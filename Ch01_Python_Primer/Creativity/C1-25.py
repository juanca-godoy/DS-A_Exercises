# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example,
# if given the string "Let's try, Mike.", this function would return "Lets try Mike".
import string


def rm_punctuation(s):
    punctuation = set(string.punctuation)
    new_string = ""
    for i in s:
        if i in punctuation:
            pass
        else:
            new_string += i
    return new_string


print(rm_punctuation("Hello."))
