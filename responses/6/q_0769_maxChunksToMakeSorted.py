class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_seen = 0

        for i, val in enumerate(arr):
            max_seen = max(max_seen, val)
            if i == max_seen:
                chunks += 1

        return chunks
