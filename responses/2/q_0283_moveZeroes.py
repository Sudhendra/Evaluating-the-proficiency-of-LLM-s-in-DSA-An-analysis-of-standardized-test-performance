class Solution:
    
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = 0
        index = 0
        
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
            else:
                zero_count += 1
        
        for i in range(index, len(nums)):
            nums[i] = 0