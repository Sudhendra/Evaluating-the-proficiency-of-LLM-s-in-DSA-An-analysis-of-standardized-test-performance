from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        
        stops_for_bus = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stops_for_bus[stop].add(bus)
        
        bfs_queue = deque([(source, 0)])
        visited_buses = set()
        visited_stops = set()
        
        while bfs_queue:
            curr_stop, num_buses = bfs_queue.popleft()
            if curr_stop == target:
                return num_buses
            
            visited_stops.add(curr_stop)
            for bus in stops_for_bus[curr_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for next_stop in routes[bus]:
                    if next_stop not in visited_stops:
                        bfs_queue.append((next_stop, num_buses+1))
        
        return -1
