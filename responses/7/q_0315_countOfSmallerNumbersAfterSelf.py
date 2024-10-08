class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        sorted_nums = []
        for i in range(len(nums)-1, -1, -1):
            index = bisect.bisect_left(sorted_nums, nums[i])
            counts[i] = index
            sorted_nums.insert(index, nums[i])
        return counts
