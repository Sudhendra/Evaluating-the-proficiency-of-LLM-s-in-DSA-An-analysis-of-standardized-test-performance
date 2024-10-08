from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        result = []
        heap = []
        
        # Initialize the heap with the first pair from nums1 and each element from nums2
        for i in range(min(k, len(nums1))):
            heap.append((nums1[i] + nums2[0], i, 0))
        
        while k > 0 and heap:
            sum_val, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            k -= 1
        
        return result
