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
        min_heap = [(0, k)]

        while min_heap:
            cur_dist, cur_node = heapq.heappop(min_heap)
            if cur_dist > distances[cur_node]:
                continue
            if cur_node in graph:
                for next_node, edge_time in graph[cur_node]:
                    if cur_dist + edge_time < distances[next_node]:
                        distances[next_node] = cur_dist + edge_time
                        heapq.heappush(min_heap, (distances[next_node], next_node))
        
        max_dist = max(distances.values())
        if max_dist == float('inf'):
            return -1
        return max_dist
