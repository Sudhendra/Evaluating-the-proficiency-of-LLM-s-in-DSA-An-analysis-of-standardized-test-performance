from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        if source == target:
            return 0

        stops_visited = set()
        buses_taken = 0
        queue = deque([source])

        while queue:
            buses_taken += 1
            stops = len(queue)

            for _ in range(stops):
                current_stop = queue.popleft()
                for route_idx in stop_to_routes[current_stop]:
                    for stop in routes[route_idx]:
                        if stop == target:
                            return buses_taken
                        if stop not in stops_visited:
                            stops_visited.add(stop)
                            queue.append(stop)
                    routes[route_idx] = []  # Mark the route as visited to avoid revisiting

        return -1
