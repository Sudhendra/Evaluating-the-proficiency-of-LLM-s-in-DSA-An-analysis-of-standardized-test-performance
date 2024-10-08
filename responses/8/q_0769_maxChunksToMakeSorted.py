from typing import List

class Solution:
    
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_chunks = 0
        max_val = 0
        for i, val in enumerate(arr):
            max_val = max(max_val, val)
            if max_val == i:
                max_chunks += 1
        return max_chunks
