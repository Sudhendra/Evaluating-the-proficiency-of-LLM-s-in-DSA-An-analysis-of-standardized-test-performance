from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        counts = [1] * n
        res = [0] * n
        
        def post_order(node, parent):
            for child in graph[node]:
                if child != parent:
                    post_order(child, node)
                    counts[node] += counts[child]
                    res[node] += res[child] + counts[child]
        
        def pre_order(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - counts[child] + (n - counts[child])
                    pre_order(child, node)
        
        post_order(0, -1)
        pre_order(0, -1)
        
        return res
