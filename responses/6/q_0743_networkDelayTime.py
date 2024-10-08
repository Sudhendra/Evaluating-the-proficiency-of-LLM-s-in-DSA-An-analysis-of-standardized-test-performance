from typing import List
import heapq

class Solution:
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        distances = {node: float('inf') for node in range(1, n+1)}
        distances[k] = 0

        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time > distances[node]:
                continue
            if node in graph:
                for next_node, next_time in graph[node]:
                    new_time = time + next_time
                    if new_time < distances[next_node]:
                        distances[next_node] = new_time
                        heapq.heappush(heap, (new_time, next_node))

        max_time = max(distances.values())
        return max_time if max_time < float('inf') else -1
