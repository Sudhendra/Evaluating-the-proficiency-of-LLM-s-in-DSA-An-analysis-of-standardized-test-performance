class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x * 10, reverse=True)  # Create a custom comparator for sorting
        return str(int("".join(nums)))  # Join sorted list and convert to string