from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_len = m + n

        while left <= right:
            partition_x = (left + right) // 2
            partition_y = (total_len + 1) // 2 - partition_x

            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if total_len % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return float(max(max_left_x, max_left_y))
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1

        raise ValueError("Input arrays are not sorted.")
