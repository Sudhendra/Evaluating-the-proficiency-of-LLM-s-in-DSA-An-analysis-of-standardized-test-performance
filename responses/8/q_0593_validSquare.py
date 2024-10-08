from typing import List

class Solution:
    def distance(self, p1: List[int], p2: List[int]) -> int:
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        points = [p1, p2, p3, p4]
        distances = []

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distances.append(self.distance(points[i], points[j]))

        distances.sort()

        return distances[0] > 0 and distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]

# Example Usage
solution = Solution()
print(solution.validSquare([0,0], [1,1], [1,0], [0,1]))  # Expected output: True
print(solution.validSquare([0,0], [1,1], [1,0], [0,12]))  # Expected output: False
print(solution.validSquare([1,0], [-1,0], [0,1], [0,-1]))  # Expected output: True
