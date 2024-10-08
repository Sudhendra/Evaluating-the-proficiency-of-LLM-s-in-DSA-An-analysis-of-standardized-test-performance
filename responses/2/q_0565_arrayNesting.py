from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        ans = 0
        
        for i in range(n):
            if not visited[i]:
                count = 0
                while not visited[i]:
                    visited[i] = True
                    i = nums[i]
                    count += 1
                ans = max(ans, count)
        
        return ans
