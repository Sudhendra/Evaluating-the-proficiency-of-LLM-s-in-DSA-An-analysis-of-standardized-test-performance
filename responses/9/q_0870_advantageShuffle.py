from collections import deque

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted(nums2)
        remaining = deque()
        assigned = {}
        
        for num in sorted_nums2:
            if num < nums1[-1]:
                assigned[num] = nums1.pop()
            else:
                remaining.append(num)
        
        return [assigned[num] if num in assigned else remaining.popleft() for num in nums2]
