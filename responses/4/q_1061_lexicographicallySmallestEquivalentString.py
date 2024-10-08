class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for ch1, ch2 in zip(s1, s2):
            union(ch1, ch2)

        smallest_str = []
        for ch in baseStr:
            smallest_str.append(find(ch))

        return "".join(smallest_str)
