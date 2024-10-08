from typing import List

class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = sum(nums) - sum(set(nums))
        missing = n*(n+1)//2 - sum(set(nums))
        return [duplicate, duplicate + missing]

    # If you have multiple solutions, add them all here as methods of the same class.
