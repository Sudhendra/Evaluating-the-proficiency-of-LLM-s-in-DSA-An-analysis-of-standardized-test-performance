class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[right]:  # Right side is sorted, minimum is on the left
                right = mid
            elif nums[mid] > nums[right]:  # Left side is sorted, minimum is on the right
                left = mid + 1
            else:  # nums[mid] == nums[right], move right boundary towards left
                right -= 1
                
        return nums[left]