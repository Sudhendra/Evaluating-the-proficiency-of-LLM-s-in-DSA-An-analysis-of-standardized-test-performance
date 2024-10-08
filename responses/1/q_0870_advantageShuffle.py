from collections import deque

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted(nums2)
        remaining = deque()

        assigned = {num: [] for num in nums2}

        j = 0
        for num in sorted_nums2:
            if num < nums1[j]:
                assigned[num].append(nums1[j])
                j += 1
            else:
                remaining.append(num)

        return [assigned[num].pop() if assigned[num] else remaining.popleft() for num in nums2]