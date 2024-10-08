from itertools import permutations
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(num):
            root = isqrt(num)
            return root * root == num

        def is_squareful(a, b):
            return is_square(a + b)

        def backtrack(curr_permutation, remaining_nums):
            if not remaining_nums:
                return 1

            count = 0
            for i in range(len(remaining_nums)):
                if i > 0 and remaining_nums[i] == remaining_nums[i-1]:
                    continue
                if not curr_permutation or is_squareful(curr_permutation[-1], remaining_nums[i]):
                    count += backtrack(curr_permutation + [remaining_nums[i]], remaining_nums[:i] + remaining_nums[i+1:])

            return count

        count = 0
        nums.sort()
        for perm in set(permutations(nums)):
            count += backtrack([], list(perm))

        return count
