class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        from collections import Counter

        counter = Counter(s)
        maxChar = max(counter, key=counter.get)
        maxCount = counter[maxChar]

        if maxCount > (len(s) + 1) // 2:
            return ""

        output = [None] * len(s)
        output[::2], output[1::2] = maxChar * maxCount, ''

        counter.pop(maxChar)

        pq = [(-val, key) for key, val in counter.items()]
        heapq.heapify(pq)

        idx = 1
        while pq:
            val, char = heapq.heappop(pq)
            while val < 0:
                if idx >= len(s):
                    idx = 0
                output[idx] = char
                val += 1
                idx += 2

        return "".join(output)