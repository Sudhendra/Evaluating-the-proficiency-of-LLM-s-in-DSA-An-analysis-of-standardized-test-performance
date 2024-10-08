class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_val = 0
        for i, val in enumerate(arr):
            max_val = max(max_val, val)
            if max_val == i:
                chunks += 1
        return chunks