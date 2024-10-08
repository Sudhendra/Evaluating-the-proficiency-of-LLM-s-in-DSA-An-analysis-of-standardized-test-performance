from typing import List

class Solution:
    
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        pairs = []
        for i in nums1:
            for j in nums2:
                pairs.append([i, j])
                
        pairs.sort(key=lambda x: sum(x))
        
        return pairs[:k]
