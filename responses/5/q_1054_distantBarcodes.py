from typing import List
from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(heap)
        
        result = []
        while len(heap) >= 2:
            first_count, first_barcode = heapq.heappop(heap)
            second_count, second_barcode = heapq.heappop(heap)
            
            result.extend([first_barcode, second_barcode])
            
            if first_count + 1:
                heapq.heappush(heap, (first_count + 1, first_barcode))
            if second_count + 1:
                heapq.heappush(heap, (second_count + 1, second_barcode))
        
        if heap:
            result.append(heap[0][1])
        
        return result