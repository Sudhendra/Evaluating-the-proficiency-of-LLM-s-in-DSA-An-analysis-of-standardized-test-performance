from collections import Counter
from heapq import heappush, heappop

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        max_heap = [(-freq, num) for num, freq in counter.items()]
        heapify(max_heap)
        result = []
        
        while len(max_heap) >= 2:
            freq1, num1 = heappop(max_heap)
            freq2, num2 = heappop(max_heap)
            result.extend([num1, num2])
            if freq1 + 1:
                heappush(max_heap, (freq1 + 1, num1))
            if freq2 + 1:
                heappush(max_heap, (freq2 + 1, num2))
        
        if max_heap:
            result.append(max_heap[0][1])
        
        return result
