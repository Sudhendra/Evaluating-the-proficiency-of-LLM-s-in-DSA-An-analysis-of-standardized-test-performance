from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        result = []
        for num in counter1.keys():
            result += [num] * min(counter1[num], counter2[num])
        return result