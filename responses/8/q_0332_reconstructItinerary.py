from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for ticket in sorted(tickets, reverse=True):
            graph[ticket[0]].append(ticket[1])
        
        route = []
        
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            route.append(node)
        
        dfs("JFK")
        
        return route[::-1]
