class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for char1, char2 in zip(s1, s2):
            union(char1, char2)

        res = []
        for char in baseStr:
            root = find(char)
            res.append(root)

        return ''.join(res)