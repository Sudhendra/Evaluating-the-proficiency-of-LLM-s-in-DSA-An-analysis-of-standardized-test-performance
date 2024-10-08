class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        res = []
        for c in baseStr:
            root = find(ord(c) - ord('a'))
            res.append(chr(root + ord('a')))

        return ''.join(res)
