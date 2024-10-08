from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        
        stop_to_routes = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].add(i)
        
        queue = deque([(source, 0)])
        visited_routes = set()
        visited_stops = set([source])
        
        while queue:
            current_stop, num_buses = queue.popleft()
            
            if current_stop == target:
                return num_buses
            
            for route_id in stop_to_routes[current_stop]:
                if route_id in visited_routes:
                    continue
                
                visited_routes.add(route_id)
                for stop in routes[route_id]:
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, num_buses + 1))
        
        return -1
