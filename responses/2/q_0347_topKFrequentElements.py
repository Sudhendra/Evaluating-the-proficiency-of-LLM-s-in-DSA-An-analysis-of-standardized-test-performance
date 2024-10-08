from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = [(-freq, num) for num, freq in freq_map.items()]
        heapq.heapify(heap)
        
        top_k = []
        for _ in range(k):
            top_k.append(heapq.heappop(heap)[1])
        
        return top_k