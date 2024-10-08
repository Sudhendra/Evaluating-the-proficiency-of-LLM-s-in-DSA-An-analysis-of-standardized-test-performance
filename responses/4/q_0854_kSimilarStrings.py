class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return ''.join(s)
        
        def dfs(s1, s2, i):
            if i == len(s1):
                return 0 if s1 == s2 else float('inf')
            
            if s1[i] == s2[i]:
                return dfs(s1, s2, i+1)
            
            res = float('inf')
            for j in range(i+1, len(s1)):
                if s1[j] == s2[i]:
                    s1 = swap(s1, i, j)
                    res = min(res, 1 + dfs(s1, s2, i+1))
                    s1 = swap(s1, i, j)  # backtracking

            return res
        
        return dfs(s1, s2, 0)
