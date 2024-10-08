from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth_element(k, nums1, nums2):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            if k == 0:
                return min(nums1[0], nums2[0])

            mid1, mid2 = len(nums1) // 2, len(nums2) // 2
            if mid1 + mid2 < k:
                if nums1[mid1] > nums2[mid2]:
                    return find_kth_element(k - mid2 - 1, nums1, nums2[mid2+1:])
                else:
                    return find_kth_element(k - mid1 - 1, nums1[mid1+1:], nums2)
            else:
                if nums1[mid1] > nums2[mid2]:
                    return find_kth_element(k, nums1[:mid1], nums2)
                else:
                    return find_kth_element(k, nums1, nums2[:mid2])

        total_len = len(nums1) + len(nums2)
        if total_len % 2:
            return find_kth_element(total_len // 2, nums1, nums2)
        else:
            return (find_kth_element(total_len // 2 - 1, nums1, nums2) + find_kth_element(total_len // 2, nums1, nums2)) / 2
