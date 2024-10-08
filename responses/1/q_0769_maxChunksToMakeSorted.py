from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count_chunks = 0
        max_element = 0
        
        for i, num in enumerate(arr):
            max_element = max(max_element, num)
            if max_element == i:
                count_chunks += 1
                
        return count_chunks
