from collections import Counter
from math import sqrt
from itertools import permutations

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_squareful(a, b):
            return int(sqrt(a + b))**2 == a + b

        def backtrack(curr_permutation, counter):
            nonlocal count
            if len(curr_permutation) == len(nums):
                count += 1
            for num in counter:
                if counter[num] > 0:
                    if not curr_permutation or is_squareful(curr_permutation[-1], num):
                        curr_permutation.append(num)
                        counter[num] -= 1
                        backtrack(curr_permutation, counter)
                        curr_permutation.pop()
                        counter[num] += 1
        
        count = 0
        counter = Counter(nums)
        backtrack([], counter)
        return count
