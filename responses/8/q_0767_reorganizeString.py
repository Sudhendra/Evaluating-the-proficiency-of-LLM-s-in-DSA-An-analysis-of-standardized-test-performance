class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter, deque
        counts = Counter(s)
        max_heap = deque(sorted(counts.items(), key=lambda x: -x[1]))
        result = []

        while len(max_heap) >= 2:
            char1, count1 = max_heap.popleft()
            char2, count2 = max_heap.popleft()
            result.extend([char1, char2])
            if count1 - 1 > 0:
                max_heap.append((char1, count1 - 1))
            if count2 - 1 > 0:
                max_heap.append((char2, count2 - 1))

        if max_heap:
            if max_heap[0][1] > 1:
                return ""
            result.append(max_heap[0][0])

        return "".join(result)
