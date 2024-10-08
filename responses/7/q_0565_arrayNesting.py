class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        longest_set = 0
        
        for i in range(len(nums)):
            if not visited[i]:
                current = i
                count = 0
                while not visited[current]:
                    visited[current] = True
                    current = nums[current]
                    count += 1
                longest_set = max(longest_set, count)
        
        return longest_set
