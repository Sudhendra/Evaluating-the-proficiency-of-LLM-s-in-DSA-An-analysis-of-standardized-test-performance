from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        
        intersection = []
        
        for num, freq in counts1.items():
            common_freq = min(freq, counts2.get(num, 0))
            intersection.extend([num] * common_freq)
        
        return intersection
