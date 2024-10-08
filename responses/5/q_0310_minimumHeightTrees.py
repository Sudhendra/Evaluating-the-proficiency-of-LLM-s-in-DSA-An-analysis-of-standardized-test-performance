from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degrees = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        leaves = deque([node for node in range(n) if degrees[node] == 1])

        while n > 2:
            n -= len(leaves)
            new_leaves = deque()

            for leaf in leaves:
                neighbor = graph[leaf][0]
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return list(leaves)
