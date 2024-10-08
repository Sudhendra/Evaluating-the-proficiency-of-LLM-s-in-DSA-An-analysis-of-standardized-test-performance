class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq

        counter = Counter(s)
        max_heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(max_heap)

        result = []
        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            result.extend([char1, char2])

            if freq1 < -1:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 < -1:
                heapq.heappush(max_heap, (freq2 + 1, char2))

        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if freq < -1:
                return ""
            result.append(char)

        return "".join(result)