from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}  # Adjacency list
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        distances = {node: float('inf') for node in range(1, n+1)}
        distances[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if dist > distances[node]:
                continue
            if node in graph:
                for nei, weight in graph[node]:
                    if dist + weight < distances[nei]:
                        distances[nei] = dist + weight
                        heapq.heappush(min_heap, (dist + weight, nei))
        
        max_distance = max(distances.values())
        return max_distance if max_distance < float('inf') else -1
