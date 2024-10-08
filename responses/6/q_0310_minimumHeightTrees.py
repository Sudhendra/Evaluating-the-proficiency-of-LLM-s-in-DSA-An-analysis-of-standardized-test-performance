from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]) -> List[int]:
        if n == 1:
            return [0]

        adj_list = defaultdict(list)
        degree = [0] * n

        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque([i for i in range(n) if degree[i] == 1])

        while n > 2:
            n -= len(leaves)
            new_leaves = deque()

            for leaf in leaves:
                neighbor = adj_list[leaf].pop()
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return list(leaves)
