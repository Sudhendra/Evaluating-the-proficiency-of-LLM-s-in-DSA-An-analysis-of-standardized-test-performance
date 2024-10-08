from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_freq = {}
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        
        max_length = 0
        for num in num_freq:
            if num + 1 in num_freq:
                max_length = max(max_length, num_freq[num] + num_freq[num + 1])
        
        return max_length