from typing import List

class Solution:
    
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        
        points = []
        for left, right, height in buildings:
            points.append((left, -height))  
            points.append((right, height))  
        
        points.sort()  
        
        result = []
        prev_height = 0
        max_heap = [0]
        
        for point in points:
            if point[1] < 0:
                heapq.heappush(max_heap, point[1])
            else:
                max_heap.remove(-point[1])
                heapq.heapify(max_heap)
                
            current_max = -max_heap[0]
            if current_max != prev_height:
                result.append([point[0], current_max])
                prev_height = current_max
        
        return result
