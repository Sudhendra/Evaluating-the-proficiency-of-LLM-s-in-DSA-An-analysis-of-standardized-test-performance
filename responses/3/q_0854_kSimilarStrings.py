class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbors(s):
            for i, c in enumerate(s):
                if c != s2[i]:
                    break
            for j in range(i + 1, len(s)):
                if s[j] == s2[i]:
                    yield s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        queue = [(s1, 0)]
        visited = {s1}
        while queue:
            s, k = queue.pop(0)
            if s == s2:
                return k
            for nei in neighbors(s):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, k + 1))
