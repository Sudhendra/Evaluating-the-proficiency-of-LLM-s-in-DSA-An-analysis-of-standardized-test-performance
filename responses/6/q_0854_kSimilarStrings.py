class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbors(s):
            for i, c in enumerate(s):
                if c != s2[i]:
                    break
            for j in range(i+1, len(s)):
                if s[j] == s2[i]:
                    yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        
        queue = collections.deque([s1])
        visited = set([s1])
        k = 0
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == s2:
                    return k
                for neighbor in neighbors(curr):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            k += 1
