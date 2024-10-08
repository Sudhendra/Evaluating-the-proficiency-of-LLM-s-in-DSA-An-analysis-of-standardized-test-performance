from typing import List

class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        def dist(p, q):
            return (p[0] - q[0])**2 + (p[1] - q[1])**2
        
        points = [p1, p2, p3, p4]
        distances = []
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = dist(points[i], points[j])
                if d == 0:
                    return False
                distances.append(d)
        
        distances.sort()
        return distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]

# Example usage
sol = Solution()
print(sol.validSquare([0,0], [1,1], [1,0], [0,1]))  # Output: True
print(sol.validSquare([0,0], [1,1], [1,0], [0,12]))  # Output: False
print(sol.validSquare([1,0], [-1,0], [0,1], [0,-1]))  # Output: True
