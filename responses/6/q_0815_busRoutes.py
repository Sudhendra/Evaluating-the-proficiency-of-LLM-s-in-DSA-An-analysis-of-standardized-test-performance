from typing import List

class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stop_to_routes = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in stop_to_routes:
                    stop_to_routes[stop] = []
                stop_to_routes[stop].append(i)

        queue = [(source, 0)]
        visited_stops = set()
        visited_routes = set()

        while queue:
            current_stop, bus_count = queue.pop(0)

            if current_stop == target:
                return bus_count

            visited_stops.add(current_stop)

            for route_index in stop_to_routes.get(current_stop, []):
                if route_index not in visited_routes:
                    for new_stop in routes[route_index]:
                        if new_stop not in visited_stops:
                            queue.append((new_stop, bus_count + 1))
                    visited_routes.add(route_index)

        return -1
