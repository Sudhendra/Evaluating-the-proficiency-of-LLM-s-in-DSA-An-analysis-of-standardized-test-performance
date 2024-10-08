from collections import Counter
from math import isqrt
from itertools import permutations

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_squareful(a, b):
            return isqrt(a + b) ** 2 == a + b
        
        def backtrack(curr_perm, remaining):
            if not remaining:
                self.count += 1
            for num in remaining:
                if not curr_perm or is_squareful(curr_perm[-1], num):
                    prev_count = count[num]
                    if prev_count > 1:
                        count[num] -= 1
                    else:
                        del count[num]
                    backtrack(curr_perm + [num], remaining - {num})
                    count[num] = prev_count
        
        count = Counter(nums)
        self.count = 0
        for num in count:
            count[num] -= 1
            backtrack([num], set(nums) - {num})
            count[num] += 1
        return self.count
