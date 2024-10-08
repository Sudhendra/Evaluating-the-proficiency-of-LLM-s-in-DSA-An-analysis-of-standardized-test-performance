class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        res = []
        assigned = {}
        for num in nums2:
            assigned[num] = assigned.get(num, []) + [nums1.pop()]
        for num in nums2:
            res.append(assigned[num].pop())
        return res
