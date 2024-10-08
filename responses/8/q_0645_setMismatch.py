from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_actual = sum(nums)
        sum_expected = n*(n+1)//2
        set_nums = set(nums)
        
        duplicate_num = sum_actual - sum(set_nums)
        missing_num = sum_expected - sum(set_nums)
        
        return [duplicate_num, missing_num]
