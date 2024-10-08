class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        
        max_heap = []
        for char, count in counter.items():
            heapq.heappush(max_heap, (-count, char))
        
        result = []
        prev_count, prev_char = 0, ''
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            count += 1
            prev_count, prev_char = count, char
        
        if len(result) == len(s):
            return ''.join(result)
        else:
            return ''
