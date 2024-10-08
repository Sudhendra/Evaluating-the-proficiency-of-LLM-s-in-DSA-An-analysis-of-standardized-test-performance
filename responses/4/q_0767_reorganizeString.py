from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-val, key) for key, val in count.items()]
        heapq.heapify(maxHeap)
        
        result = []
        prevCount, prevChar = 0, ''
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            result.append(char)
            if prevCount < 0:
                heapq.heappush(maxHeap, (prevCount, prevChar))
            count += 1
            prevCount, prevChar = count, char
        
        result = ''.join(result)
        
        return result if len(result) == len(s) else ''
