from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(-count, num) for num, count in counts.items()]
        heapq.heapify(heap)
        
        top_k = []
        for _ in range(k):
            top_k.append(heapq.heappop(heap)[1])
        
        return top_k
