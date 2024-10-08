from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if not visited[i]:
                start = nums[i]
                length = 0
                while not visited[start]:
                    visited[start] = True
                    start = nums[start]
                    length += 1
                max_length = max(max_length, length)

        return max_length
