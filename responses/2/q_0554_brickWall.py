class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = collections.defaultdict(int)
        for row in wall:
            prefix_sum = 0
            for brick in row[:-1]:
                prefix_sum += brick
                count[prefix_sum] += 1
        return len(wall) - max(count.values(), default=0)
