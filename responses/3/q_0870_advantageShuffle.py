from collections import deque

class Solution:
    
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted((num, index) for index, num in enumerate(nums2))
        
        high_nums1 = deque()
        low_nums1 = deque()
        
        for num, index in sorted_nums2:
            if nums1[-1] > num:
                high_nums1.append(nums1.pop())
            else:
                low_nums1.append(nums1.pop())
        
        result = []
        for num, index in sorted_nums2:
            if high_nums1:
                result.append(high_nums1.pop())
            else:
                result.append(low_nums1.pop())
        
        return result
