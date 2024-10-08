from typing import List

class Solution:
    
    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        corner_set = set() # Set to store all corner points
        area_sum = 0  # Sum of areas of all rectangles
        corner_dict = {} # Dictionary to store counts of corner points
        
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            area_sum += (x2 - x1) * (y2 - y1)
            
            # Store corner points in a set
            for corner in [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]:
                if corner in corner_set:
                    corner_dict[corner] += 1
                else:
                    corner_set.add(corner)
                    corner_dict[corner] = 1
        
        # Find the four corners of the big rectangle
        big_rect_corners = [(min_x, min_y), (max_x, min_y), (min_x, max_y), (max_x, max_y)] \
                            if len(rectangles) > 0 else [(0, 0), (0, 0), (0, 0), (0, 0)]
        
        for corner in big_rect_corners:
            if corner not in corner_set or corner_dict[corner] != 1:
                return False
        
        # Check if the total area matches
        min_x, min_y = min(corner_set, key=lambda x: (x[0], x[1]))
        max_x, max_y = max(corner_set, key=lambda x: (x[0], x[1]))
        return area_sum == (max_x - min_x) * (max_y - min_y)
