from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        
        intersection = []
        
        for num, count in counts1.items():
            if num in counts2:
                intersection.extend([num] * min(count, counts2[num]))
        
        return intersection
