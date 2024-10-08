from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for ticket in tickets:
            adj_list[ticket[0]].append(ticket[1])
        
        for key in adj_list:
            adj_list[key].sort(reverse=True)
        
        stack = ["JFK"]
        route = []
        
        while stack:
            curr_node = stack[-1]
            if curr_node in adj_list and len(adj_list[curr_node]) > 0:
                stack.append(adj_list[curr_node].pop())
            else:
                route.append(stack.pop())
        
        return route[::-1]
