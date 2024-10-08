from typing import List
from collections import defaultdict
import heapq

class Solution:
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[k] = 0
        min_heap = [(0, k)]
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time > dist[node]:
                continue
            for nei, nei_time in graph[node]:
                if time + nei_time < dist[nei]:
                    dist[nei] = time + nei_time
                    heapq.heappush(min_heap, (time + nei_time, nei))
        
        max_time = max(dist.values())
        return max_time if max_time < float('inf') else -1
