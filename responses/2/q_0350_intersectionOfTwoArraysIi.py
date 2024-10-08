class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        result = []
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        for num in counter1.keys():
            result.extend([num] * min(counter1[num], counter2[num]))
        return result