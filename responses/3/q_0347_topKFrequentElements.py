from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        heap = [(-freq, num) for num, freq in frequency_map.items()]
        heapq.heapify(heap)
        
        topk = [heapq.heappop(heap)[1] for _ in range(k)]
        return topk
