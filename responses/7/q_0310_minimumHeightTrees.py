from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        graph = defaultdict(list)
        indegree = [0] * n

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1

        leaves = deque()
        for i in range(n):
            if indegree[i] == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)
