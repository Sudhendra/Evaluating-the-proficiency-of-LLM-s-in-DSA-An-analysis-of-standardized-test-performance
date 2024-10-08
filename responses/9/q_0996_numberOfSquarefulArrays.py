from itertools import permutations
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(num):
            return num == isqrt(num) ** 2

        def is_squareful(pair):
            return is_square(pair[0] + pair[1])

        count = 0
        nums.sort()
        
        def backtrack(temp, used):
            nonlocal count
            if len(temp) == len(nums):
                count += 1
                return
            
            for i in range(len(nums)):
                if i in used or (i > 0 and nums[i] == nums[i-1] and i-1 not in used):
                    continue
                if temp and not is_squareful((temp[-1], nums[i])):
                    continue

                used.add(i)
                temp.append(nums[i])
                backtrack(temp, used)
                used.remove(i)
                temp.pop()

        backtrack([], set())
        return count
