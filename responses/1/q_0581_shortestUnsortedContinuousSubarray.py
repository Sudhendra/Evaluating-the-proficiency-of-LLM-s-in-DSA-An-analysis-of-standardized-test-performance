class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = None
        end = None
        
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if start is None:
                    start = i
                end = i
        
        if start is None:
            return 0
        
        return end - start + 1
