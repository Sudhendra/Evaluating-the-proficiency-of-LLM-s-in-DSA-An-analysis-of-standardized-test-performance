class Solution:
    """An array is **monotonic** if it is either monotone increasing or monotone decreasing.

    An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

    Given an integer array `nums`, return `true` *if the given array is monotonic, or* `false` *otherwise*.
    """

    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                increasing = False
            if nums[i-1] < nums[i]:
                decreasing = False
        
        return increasing or decreasing