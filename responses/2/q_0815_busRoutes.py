class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        queue = deque([(source, 0)])  # (current_stop, bus_changes)
        visited_stops = set([source])
        visited_routes = set()

        while queue:
            current_stop, bus_changes = queue.popleft()

            for route_id in stop_to_routes[current_stop]:
                if route_id in visited_routes:
                    continue

                visited_routes.add(route_id)

                for next_stop in routes[route_id]:
                    if next_stop in visited_stops:
                        continue

                    if next_stop == target:
                        return bus_changes + 1

                    visited_stops.add(next_stop)
                    queue.append((next_stop, bus_changes + 1))

        return -1