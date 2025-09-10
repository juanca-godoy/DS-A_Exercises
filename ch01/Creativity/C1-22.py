# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.

listA = [1, 2, 3, 5, 10]
listB = [3, 2, 1, 4, 5]
n = len(listA)
listC = [(listA[i] * listB[i]) for i in range(n)]

print(listC)
