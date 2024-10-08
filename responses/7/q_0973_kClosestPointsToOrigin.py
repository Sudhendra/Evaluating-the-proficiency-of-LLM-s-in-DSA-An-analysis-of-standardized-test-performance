from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate the Euclidean distance for each point
        distances = [[point, distance(point)] for point in points]
        
        # Sort the distances based on the distance from origin
        distances.sort(key=lambda x: x[1])
        
        # Return the k closest points
        return [dist[0] for dist in distances[:k]]

def distance(point):
    return point[0]**2 + point[1]**2  # Euclidean distance calculation
