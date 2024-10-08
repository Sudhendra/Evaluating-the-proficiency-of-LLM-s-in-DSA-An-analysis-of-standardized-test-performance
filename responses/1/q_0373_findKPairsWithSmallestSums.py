from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        result = []
        heap = []
        
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(heap, (num1 + num2, num1, num2))
        
        for _ in range(min(k, len(nums1)*len(nums2))):
            _, num1, num2 = heapq.heappop(heap)
            result.append([num1, num2])
        
        return result
