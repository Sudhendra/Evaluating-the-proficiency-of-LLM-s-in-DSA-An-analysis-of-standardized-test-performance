class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = -1, -2
        min_val = nums[-1]
        max_val = nums[0]

        for i in range(1, n):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[n - 1 - i])

            if nums[i] < max_val:
                end = i

            if nums[n - 1 - i] > min_val:
                start = n - 1 - i

        return end - start + 1
