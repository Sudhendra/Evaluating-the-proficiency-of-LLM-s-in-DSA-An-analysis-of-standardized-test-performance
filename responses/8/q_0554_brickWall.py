from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges_count = defaultdict(int)
        for row in wall:
            prefix_sum = 0
            for brick in row[:-1]:
                prefix_sum += brick
                edges_count[prefix_sum] += 1
        max_edges = max(edges_count.values()) if edges_count else 0
        return len(wall) - max_edges
