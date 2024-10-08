from collections import Counter
from heapq import heappush, heappop

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        heap = [(-freq, num) for num, freq in count.items()]
        heapify(heap)
        
        result = []
        while len(heap) > 1:
            freq1, num1 = heappop(heap)
            freq2, num2 = heappop(heap)
            
            result.extend([num1, num2])
            
            if freq1 + 1 < 0:
                heappush(heap, (freq1 + 1, num1))
            if freq2 + 1 < 0:
                heappush(heap, (freq2 + 1, num2))
        
        if heap:
            result.append(heap[0][1])
        
        return result
