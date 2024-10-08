from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        heap = []
        for num1 in nums1:
            for num2 in nums2:
                # We add the negative sum to heap so we can pop the smallest sum pairs
                heapq.heappush(heap, (-(num1 + num2), [num1, num2]))
                
                if len(heap) > k:
                    heapq.heappop(heap)
        
        res = [pair[1] for pair in heap]
        return res
