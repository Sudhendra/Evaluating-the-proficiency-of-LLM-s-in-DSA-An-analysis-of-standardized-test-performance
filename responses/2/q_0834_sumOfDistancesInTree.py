from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        subtree_sizes = [1] * n
        total_distances = [0] * n
        
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    subtree_sizes[node] += subtree_sizes[child]
                    total_distances[node] += total_distances[child] + subtree_sizes[child]
        
        def calculate_distances(node, parent):
            for child in graph[node]:
                if child != parent:
                    total_distances[child] = total_distances[node] - subtree_sizes[child] + (n - subtree_sizes[child])
                    calculate_distances(child, node)
        
        dfs(0, -1)
        calculate_distances(0, -1)
        
        return total_distances
