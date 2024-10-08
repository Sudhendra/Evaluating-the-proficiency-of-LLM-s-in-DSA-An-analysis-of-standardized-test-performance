class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_length = 0
        visited = [False] * len(nums)

        for num in nums:
            if not visited[num]:
                length = 0
                while not visited[num]:
                    visited[num] = True
                    num = nums[num]
                    length += 1
                max_length = max(max_length, length)

        return max_length
