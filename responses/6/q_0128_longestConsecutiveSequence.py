from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_length = 1
                
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_length += 1
                
                max_length = max(max_length, curr_length)
        
        return max_length
