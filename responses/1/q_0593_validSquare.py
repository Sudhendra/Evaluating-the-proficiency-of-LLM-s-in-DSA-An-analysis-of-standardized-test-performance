from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(point1, point2):
            return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
        
        def is_valid_side_length(sides):
            return len(set(sides)) == 2
        
        def is_valid_diagonal_length(sides, diagonals):
            return diagonals[0] == diagonals[1] == sum(sides)
        
        def is_valid_angle(dot_product):
            return dot_product == 0
        
        points = [p1, p2, p3, p4]
        sides = [dist(points[i], points[j]) for i in range(4) for j in range(i+1, 4)]
        diagonals = [dist(p1, p3), dist(p2, p4)]
        side_length_valid = is_valid_side_length(sides)
        diagonal_length_valid = is_valid_diagonal_length(sides, diagonals)
        angle_valid = is_valid_angle(sum([(points[(i+2)%4][k] - points[i][k]) * (points[(i+3)%4][k] - points[(i+1)%4][k]) for i in range(4) for k in range(2)]))
        
        return side_length_valid and diagonal_length_valid and angle_valid
