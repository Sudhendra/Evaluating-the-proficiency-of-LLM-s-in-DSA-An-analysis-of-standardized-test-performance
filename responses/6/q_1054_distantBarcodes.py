from collections import Counter
from heapq import heappush, heappop

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        heap = []
        for num, freq in counter.items():
            heappush(heap, (-freq, num))

        result = []
        while len(heap) > 1:
            freq1, num1 = heappop(heap)
            freq2, num2 = heappop(heap)

            result.extend([num1, num2])
            if freq1 + 1: heappush(heap, (freq1 + 1, num1))
            if freq2 + 1: heappush(heap, (freq2 + 1, num2))

        if heap:
            freq, num = heappop(heap)
            while freq < 0:
                result.append(num)
                freq += 1

        return result
