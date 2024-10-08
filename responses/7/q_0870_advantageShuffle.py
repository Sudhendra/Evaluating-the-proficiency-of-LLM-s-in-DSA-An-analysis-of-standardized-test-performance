from collections import deque

class Solution:
    
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        queue = deque(sorted(nums2))
        result = [-1] * len(nums1)
        
        low, high = 0, len(nums1) - 1
        
        for num in nums1:
            if num > queue[0]:
                result[high] = num
                high -= 1
            else:
                result[low] = num
                low += 1
        return result
