from typing import List
from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_route_map = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in stop_to_route_map:
                    stop_to_route_map[stop] = []
                stop_to_route_map[stop].append(i)
        
        if source == target:
            return 0
        
        visited = set()
        queue = deque([(source, 0)])
        
        while queue:
            stop, bus_changes = queue.popleft()
            if stop == target:
                return bus_changes
            
            for route_index in stop_to_route_map.get(stop, []):
                for next_stop in routes[route_index]:
                    if next_stop not in visited:
                        visited.add(next_stop)
                        queue.append((next_stop, bus_changes + 1))
                
                routes[route_index] = []  # Mark the route as visited to avoid revisiting
                
        return -1