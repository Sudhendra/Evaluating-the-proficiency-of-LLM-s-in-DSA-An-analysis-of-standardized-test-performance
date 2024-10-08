class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                duplicates.append(abs(num))
            else:
                nums[idx] *= -1
        
        return duplicates