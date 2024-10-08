from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return self.findKth(nums1, nums2, total_len // 2)
        else:
            return (self.findKth(nums1, nums2, total_len // 2 - 1) + self.findKth(nums1, nums2, total_len // 2)) / 2

    def findKth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        len1, len2 = len(nums1), len(nums2)
        if k == 0:
            return min(nums1[0], nums2[0])

        mid1, mid2 = len1 // 2, len2 // 2
        if mid1 + mid2 < k:
            if nums1[mid1] > nums2[mid2]:
                return self.findKth(nums1, nums2[mid2 + 1:], k - mid2 - 1)
            else:
                return self.findKth(nums1[mid1 + 1:], nums2, k - mid1 - 1)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.findKth(nums1[:mid1], nums2, k)
            else:
                return self.findKth(nums1, nums2[:mid2], k)
