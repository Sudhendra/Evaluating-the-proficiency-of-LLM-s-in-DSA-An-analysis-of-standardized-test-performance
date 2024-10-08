class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 0
        
        for i in range(len(nums)):
            if nums[i] != -1:
                start = nums[i]
                count = 0
                while nums[start] != -1:
                    temp = start
                    start = nums[start]
                    count += 1
                    nums[temp] = -1
                max_length = max(max_length, count)
        
        return max_length