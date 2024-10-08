class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            while left < mid and nums[left] == nums[mid]: # Skip duplicates
                left += 1
            
            if nums[left] <= nums[mid]: # Left half is sorted
                if nums[left] <= target < nums[mid]: # Target is in left half
                    right = mid - 1
                else:
                    left = mid + 1
            else: # Right half is sorted
                if nums[mid] < target <= nums[right]: # Target is in right half
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False