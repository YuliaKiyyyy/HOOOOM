"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def Kortej():
    A = [-25, -1, 87]
    B = [-39, 0, 38]
    C = [1, 45, 55]
    D = [0, 100, 85]
    count = 0 #created an empty variable in which we write the number of sums equal to 0

    for i in A:
        for j in B:
            for k in C:
                for l in D: #did 4 rounds
                    if i + j + k + l == 0: #A[i] + B[j] + C[k] + D[l]
                        count += 1 #if the sum is 0, then the values are displayed and the variable count is incremented by 1
    return count
Kortej()

