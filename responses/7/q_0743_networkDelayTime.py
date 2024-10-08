class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        import collections

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]
        dist = {}
        
        while pq:
            time, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = time
            for nei, delay in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (time + delay, nei))
        
        if len(dist) == n:
            return max(dist.values())
        return -1
