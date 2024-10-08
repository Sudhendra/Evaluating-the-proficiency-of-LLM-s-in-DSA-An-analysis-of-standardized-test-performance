from collections import defaultdict
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted(nums2)
        remaining = defaultdict(list)
        no_match = []

        j = 0
        for num in sorted_nums2:
            if nums1[j] > num:
                remaining[num].append(nums1[j])
                j += 1
            else:
                no_match.append(nums1[j])

        return [remaining[num].pop() if remaining[num] else no_match.pop() for num in nums2]
