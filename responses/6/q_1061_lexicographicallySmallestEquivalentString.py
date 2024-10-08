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
            px, py = find(x), find(y)
            if px < py:
                parent[py] = px
            elif py < px:
                parent[px] = py

        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = []
        for letter in baseStr:
            res.append(find(letter))

        return ''.join(res)

# Test cases
solution = Solution()
assert solution.smallestEquivalentString("parker", "morris", "parser") == "makkek"
assert solution.smallestEquivalentString("hello", "world", "hold") == "hdld"
assert solution.smallestEquivalentString("leetcode", "programs", "sourcecode") == "aauaaaaada"
