from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            graph[u].append(v)
        
        route = []
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            route.append(node)
        
        dfs('JFK')
        return route[::-1]
