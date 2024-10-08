class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:  # If s1 and s2 are equal, then k is 0
            return 0

        def neighbors(s):
            n = len(s)
            for i in range(n):
                if s[i] != s2[i]:  # Find the first differing character
                    break

            chars = set()
            for j in range(i + 1, n):
                if s[j] == s2[i] and s[j] != s2[j]:  # Find the characters that can be swapped with s[i]
                    new_s = list(s)
                    new_s[i], new_s[j] = new_s[j], new_s[i]
                    yield ''.join(new_s)

        queue = [(s1, 0)]
        visited = set([s1])
        while queue:
            current, k = queue.pop(0)
            if current == s2:
                return k

            for neighbor in neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, k + 1))

        return -1  # If for some reason, we can't transform s1 to s2

# Time complexity: O(n!*n), where n is the length of the input strings s1 and s2
# Space complexity: O(n!), where n is the length of the input strings s1 and s2
