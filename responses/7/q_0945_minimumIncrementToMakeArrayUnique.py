from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        counter = [0] * (2 * 10**5 + 1)
        moves = 0
        taken = set()
        
        for num in nums:
            if num in taken:
                i = num + 1
                while i in taken:
                    i += 1
                moves += i - num
                taken.add(i)
            else:
                taken.add(num)
            counter[num] += 1
        
        return moves
