from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        max_length = 0

        for i in range(len(nums)):
            if not visited[i]:
                start = nums[i]
                count = 0
                while not visited[start]:
                    visited[start] = True
                    count += 1
                    start = nums[start]
                max_length = max(max_length, count)

        return max_length
