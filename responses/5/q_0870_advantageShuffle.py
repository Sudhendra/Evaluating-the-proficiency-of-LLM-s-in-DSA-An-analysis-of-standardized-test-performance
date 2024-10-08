from collections import deque

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted(nums2)

        remaining = deque()
        assigned = {}

        for num2 in sorted_nums2:
            if num2 < nums1[-1]:
                assigned[num2] = nums1.pop()
            else:
                remaining.append(num2)

        return [assigned[num2] if num2 in assigned else remaining.popleft() for num2 in nums2]
