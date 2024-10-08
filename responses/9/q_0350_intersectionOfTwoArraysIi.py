from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        result = []
        for num in count1.keys():
            if num in count2:
                result += [num] * min(count1[num], count2[num])
                
        return result
