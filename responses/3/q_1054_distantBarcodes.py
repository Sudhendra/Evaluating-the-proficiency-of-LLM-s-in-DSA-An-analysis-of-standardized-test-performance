from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        max_heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(max_heap)
        
        result = []
        prev = None
        
        while max_heap:
            freq, barcode = heapq.heappop(max_heap)
            result.append(barcode)
            freq += 1
            
            if prev:
                heapq.heappush(max_heap, prev)
            if freq < 0:
                prev = (freq, barcode)
            else:
                prev = None
        
        return result
