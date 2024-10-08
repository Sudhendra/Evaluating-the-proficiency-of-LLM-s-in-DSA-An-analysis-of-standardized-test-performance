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
        visited_routes = set()
        visited_stops = set([source])

        while queue:
            stop, buses_taken = queue.popleft()
            if stop == target:
                return buses_taken

            for route_idx in stop_to_routes[stop]:
                if route_idx not in visited_routes:
                    visited_routes.add(route_idx)
                    for next_stop in routes[route_idx]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses_taken + 1))

        return -1
