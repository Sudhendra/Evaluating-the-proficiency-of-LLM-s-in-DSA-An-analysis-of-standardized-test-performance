from collections import defaultdict

class Solution:
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for source in graph:
            graph[source].sort(reverse=True)
        
        def dfs(node):
            if node in graph:
                while graph[node]:
                    next_node = graph[node].pop()
                    dfs(next_node)
            result.append(node)
        
        result = []
        dfs("JFK")
        return result[::-1]
