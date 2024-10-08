class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
        
        parent = {c: c for c in range(26)}
        
        for a, b in zip(s1, s2):
            union(parent, ord(a) - ord('a'), ord(b) - ord('a'))
        
        result = []
        for char in baseStr:
            result.append(chr(find(parent, ord(char) - ord('a')) + ord('a')))
        
        return "".join(result)
