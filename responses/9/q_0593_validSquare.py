from typing import List

class Solution:
    def dist(self, p1: List[int], p2: List[int]) -> int:
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        points = [p1, p2, p3, p4]
        dists = [self.dist(points[i], points[j]) for i in range(4) for j in range(i+1, 4)]
        dists.sort()
        
        return all(d != 0 for d in dists[:4]) and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]

# Example test cases
sol = Solution()
print(sol.validSquare([0,0], [1,1], [1,0], [0,1]))  # Output: true
print(sol.validSquare([0,0], [1,1], [1,0], [0,12]))  # Output: false
print(sol.validSquare([1,0], [-1,0], [0,1], [0,-1]))  # Output: true
