from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        
        for src in graph:
            graph[src] = sorted(graph[src], reverse=True)
        
        stack = ['JFK']
        itinerary = []
        
        while stack:
            top = stack[-1]
            if top in graph and graph[top]:
                stack.append(graph[top].pop())
            else:
                itinerary.append(stack.pop())
        
        return itinerary[::-1]
