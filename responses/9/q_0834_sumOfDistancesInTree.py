from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        count = [1] * n
        total = [0] * n
        
        def post_order(node, parent):
            for child in tree[node]:
                if child == parent:
                    continue
                post_order(child, node)
                
                count[node] += count[child]
                total[node] += total[child] + count[child]
        
        def pre_order(node, parent):
            for child in tree[node]:
                if child == parent:
                    continue
                total[child] = total[node] - count[child] + n - count[child]
                pre_order(child, node)
        
        post_order(0, -1)
        pre_order(0, -1)
        
        return total
