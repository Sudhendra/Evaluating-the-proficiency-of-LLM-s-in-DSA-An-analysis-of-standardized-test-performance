from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return 1 if a+b > b+a else -1
        
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(compare), reverse=True)
        
        return str(int("".join(nums)))
