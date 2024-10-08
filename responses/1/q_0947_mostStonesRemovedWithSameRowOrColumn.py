class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for i, (x, y) in enumerate(stones):
            rows[x].add(i)
            cols[y].add(i)

        def dfs(i):
            visited.add(i)
            for j in rows[stones[i][0]] | cols[stones[i][1]]:
                if j not in visited:
                    dfs(j)

        visited = set()
        components = 0

        for i in range(len(stones)):
            if i not in visited:
                components += 1
                dfs(i)

        return len(stones) - components