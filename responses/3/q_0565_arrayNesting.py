from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                start = nums[i]
                count = 0
                while not visited[start]:
                    visited[start] = True
                    count += 1
                    start = nums[start]
                ans = max(ans, count)

        return ans
