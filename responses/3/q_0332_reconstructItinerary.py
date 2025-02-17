from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        
        for key in graph:
            graph[key] = sorted(graph[key], reverse=True)
        
        stack = ["JFK"]
        result = []
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            result.append(stack.pop())
        
        return result[::-1]