"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
    bugyg7
"""
from typing import List

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3 #length of examined subsequences
def findmaximalsubarraysum(nums: List[int], k: int) -> int:
    result = 0 #variable, for counting
    while k > 0: #while k is greater than zero, the loop is executed
        Max = max(nums)
        result = result + Max
        nums.remove(Max)
        k -= 1
    return result
findmaximalsubarraysum(nums,k)
