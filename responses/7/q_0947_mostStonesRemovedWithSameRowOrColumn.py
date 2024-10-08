class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x, y):
            visited.add((x, y))
            for next_x, next_y in rows[x] | cols[y]:
                if (next_x, next_y) not in visited:
                    dfs(next_x, next_y)

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        for i, (x, y) in enumerate(stones):
            rows[x].add((x, y))
            cols[y].add((x, y))

        visited = set()
        components = 0
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                components += 1

        return len(stones) - components
