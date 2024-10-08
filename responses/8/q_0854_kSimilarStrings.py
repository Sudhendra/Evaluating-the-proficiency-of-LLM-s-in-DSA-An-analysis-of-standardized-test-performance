from collections import deque

class Solution:
    
    def kSimilarity(self, s1: str, s2: str) -> int:
        def get_neighbors(s):
            i = 0
            while i < len(s) and s[i] == s2[i]:
                i += 1
            for j in range(i + 1, len(s)):
                if s[j] == s2[i]:
                    yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

        queue = deque([(s1, 0)])
        visited = set([s1])
        
        while queue:
            word, swaps = queue.popleft()
            if word == s2:
                return swaps
            for neighbor in get_neighbors(word):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, swaps + 1))

solution = Solution()
s1 = "abc"
s2 = "bca"
print(solution.kSimilarity(s1, s2))  # Output: 2
