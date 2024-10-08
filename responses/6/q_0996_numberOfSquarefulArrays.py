from itertools import permutations
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(num):
            return isqrt(num) ** 2 == num

        def can_chain(prev, next_num):
            return is_square(prev + next_num)

        def backtrack(curr_permutation, remaining_nums):
            if len(remaining_nums) == 0:
                nonlocal count
                count += 1
                return

            for i, next_num in enumerate(remaining_nums):
                if i > 0 and remaining_nums[i] == remaining_nums[i - 1]:
                    continue
                if len(curr_permutation) == 0 or can_chain(curr_permutation[-1], next_num):
                    backtrack(curr_permutation + [next_num], remaining_nums[:i] + remaining_nums[i+1:])

        count = 0
        nums.sort()
        backtrack([], nums)

        return count
