class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                if rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                elif rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        parent = [i for i in range(26)]
        rank = [0] * 26

        for a, b in zip(s1, s2):
            union(parent, rank, ord(a) - 97, ord(b) - 97)

        result = []
        for char in baseStr:
            root = find(parent, ord(char) - 97)
            result.append(chr(root + 97))

        return ''.join(result)
