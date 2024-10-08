class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        from collections import Counter
        counts = Counter(s)
        max_heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(max_heap)
        
        result = []
        while len(max_heap) >= 2:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)
            result.extend([char1, char2])
            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))
            
        if max_heap:
            count, char = heapq.heappop(max_heap)
            if count < -1:
                return ""
            result.append(char)
        
        return "".join(result)