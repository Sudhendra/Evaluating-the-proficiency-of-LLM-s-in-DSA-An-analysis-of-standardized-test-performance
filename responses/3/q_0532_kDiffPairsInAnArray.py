class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        unique_nums = set(nums)
        
        if k == 0:
            count = sum(1 for num in unique_nums if nums.count(num) > 1)
        else:
            count = sum(1 for num in unique_nums if num + k in unique_nums)
        
        return count