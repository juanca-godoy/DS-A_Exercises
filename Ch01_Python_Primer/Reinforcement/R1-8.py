# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# n≤k<0, what is the equivalent index j ≥0 such that s[j] references
# the same element?

print(
    "If a string s has length n, and you use negative index K with -n <= k < 0,\n",
    "the equivalent non-negative index j is j = n + k, so that s[j] and s[k] reference the same element.\n",
)

s = "Hello"
n = len(s)
k = -2
j = k + n

print(f"The negative index s[k] is {s[k]}, and the positive index s[j] is {s[j]}")
