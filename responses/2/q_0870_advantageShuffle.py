from collections import deque

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted(nums2)
        remaining = deque()
        assigned = {}

        for n in sorted_nums2:
            if n < nums1[-1]:
                assigned[n] = nums1.pop()
            else:
                remaining.append(n)

        return [assigned.get(n, remaining.popleft()) for n in nums2]
