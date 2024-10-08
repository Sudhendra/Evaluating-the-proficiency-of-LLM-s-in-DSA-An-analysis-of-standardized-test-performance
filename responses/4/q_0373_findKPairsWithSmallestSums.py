from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(heap, (num1 + num2, [num1, num2]))

        result = []
        while heap and len(result) < k:
            result.append(heapq.heappop(heap)[1])

        return result
