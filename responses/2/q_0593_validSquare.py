class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        
        points = [p1, p2, p3, p4]
        distances = []
        
        for i in range(4):
            for j in range(i + 1, 4):
                if p1 != p2:
                    distances.append(dist(points[i], points[j]))
        
        distances.sort()
        
        return distances[0] > 0 and distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]