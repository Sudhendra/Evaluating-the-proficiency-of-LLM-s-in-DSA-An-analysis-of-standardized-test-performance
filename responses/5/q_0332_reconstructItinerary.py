from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])

        for src in graph:
            graph[src].sort(reverse=True)

        itinerary = []
        def dfs(node):
            while graph[node]:
                next_dest = graph[node].pop()
                dfs(next_dest)
            itinerary.append(node)

        dfs("JFK")
        return itinerary[::-1]
