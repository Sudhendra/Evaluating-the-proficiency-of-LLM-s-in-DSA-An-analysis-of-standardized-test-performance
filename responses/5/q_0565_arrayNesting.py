from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(index):
            count = 0
            while nums[index] != -1:
                temp = index
                index = nums[index]
                nums[temp] = -1
                count += 1
            return count

        max_length = 0
        for i in range(len(nums)):
            if nums[i] != -1:
                max_length = max(max_length, dfs(i))
        return max_length
