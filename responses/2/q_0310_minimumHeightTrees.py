class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]) -> List[int]:
        if n == 1:
            return [0]

        adj_list = defaultdict(list)
        degrees = defaultdict(int)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        leaves = [node for node in degrees if degrees[node] == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = adj_list[leaf][0]
                adj_list[neighbor].remove(leaf)
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves