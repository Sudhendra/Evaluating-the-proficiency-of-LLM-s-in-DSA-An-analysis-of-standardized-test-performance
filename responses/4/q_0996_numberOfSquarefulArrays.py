from typing import List
from math import sqrt
from collections import Counter
from itertools import permutations

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(num):
            sqrt_num = int(sqrt(num))
            return sqrt_num * sqrt_num == num

        def dfs(remaining_counts, prev_num):
            if sum(remaining_counts.values()) == 0:
                return 1

            total_perms = 0
            for num in remaining_counts:
                if remaining_counts[num] == 0:
                    continue

                if prev_num == -1 or is_square(prev_num + num):
                    remaining_counts[num] -= 1
                    total_perms += dfs(remaining_counts, num)
                    remaining_counts[num] += 1

            return total_perms

        counts = Counter(nums)
        return dfs(counts, -1)
