from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_routes = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].add(i)
        
        queue = deque([(source, 0)])
        visited_buses = set()
        visited_stops = set()
        
        while queue:
            stop, bus_changes = queue.popleft()
            
            for bus in stop_to_routes[stop]:
                if bus in visited_buses:
                    continue
                
                visited_buses.add(bus)
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return bus_changes + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, bus_changes + 1))
        
        return -1
