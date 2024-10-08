class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        duplicate = sum(nums) - sum(set(nums))
        missing = total_sum - actual_sum + duplicate
        return [duplicate, missing]