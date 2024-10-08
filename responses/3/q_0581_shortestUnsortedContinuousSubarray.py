class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        start = 0
        end = n - 1

        # Find the first index where sorted array and input array differ
        while start < n and nums[start] == sorted_nums[start]:
            start += 1

        # If the entire array is sorted
        if start == n:
            return 0

        # Find the last index where sorted array and input array differ
        while end >= 0 and nums[end] == sorted_nums[end]:
            end -= 1

        return end - start + 1