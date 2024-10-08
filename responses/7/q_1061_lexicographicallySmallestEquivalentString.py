class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            parent[root_x] = min(root_x, root_y)

        for i in range(len(s1)):
            union(s1[i], s2[i])

        result = []
        for char in baseStr:
            result.append(find(char))

        return ''.join(result)

# Example usage
sol = Solution()
print(sol.smallestEquivalentString("parker", "morris", "parser"))  # Output: "makkek"
print(sol.smallestEquivalentString("hello", "world", "hold"))  # Output: "hdld"
print(sol.smallestEquivalentString("leetcode", "programs", "sourcecode"))  # Output: "aauaaaaada"
