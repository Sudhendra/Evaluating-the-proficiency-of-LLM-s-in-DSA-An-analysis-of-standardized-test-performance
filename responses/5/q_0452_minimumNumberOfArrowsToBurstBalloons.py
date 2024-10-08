class Solution:
    def findMinArrowShots(self, points: List[List[int]) -> int:
        if not points:
            return 0
        
        # Sort points based on end values in ascending order
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]
        
        for start, balloon_end in points:
            if start > end:
                arrows += 1
                end = balloon_end
        
        return arrows