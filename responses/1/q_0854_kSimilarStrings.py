from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbors(s, target):
            for i, c in enumerate(s):
                if c != target[i]:
                    break
            for j in range(i+1, len(s)):
                if s[j] == target[i]:
                    yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        queue = deque([(s1, 0)])
        visited = set([s1])
        while queue:
            current, swaps = queue.popleft()
            if current == s2:
                return swaps
            for neighbor in neighbors(current, s2):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, swaps + 1))
        return -1
