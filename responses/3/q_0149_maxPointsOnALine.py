class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            
            if dx == 0:
                return (0, 1)  # vertical line, represented as (0, 1)
            elif dy == 0:
                return (1, 0)  # horizontal line, represented as (1, 0)
            
            gcd_val = gcd(abs(dx), abs(dy))
            return (dx // gcd_val, dy // gcd_val)
        
        max_points = 0
        
        for i in range(len(points) - 1):
            slopes = defaultdict(int)
            overlapping_points = 0
            local_max = 0
            
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    overlapping_points += 1
                    continue
                
                current_slope = slope(points[i], points[j])
                slopes[current_slope] += 1
                local_max = max(local_max, slopes[current_slope])
            
            max_points = max(max_points, local_max + overlapping_points + 1)
        
        return max_points