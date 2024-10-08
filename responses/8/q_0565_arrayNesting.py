from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        longest_length = 0

        for i in range(n):
            if not visited[i]:
                current = i
                length = 0
                while not visited[current]:
                    visited[current] = True
                    current = nums[current]
                    length += 1
                longest_length = max(longest_length, length)

        return longest_length
