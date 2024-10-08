from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for fromi, toi in tickets:
            if fromi not in graph:
                graph[fromi] = []
            graph[fromi].append(toi)
        
        for key in graph:
            graph[key].sort(reverse=True)
        
        stack = ["JFK"]
        itinerary = []
        
        while stack:
            curr = stack[-1]
            if curr in graph and graph[curr]:
                stack.append(graph[curr].pop())
            else:
                itinerary.append(stack.pop())
        
        return itinerary[::-1]