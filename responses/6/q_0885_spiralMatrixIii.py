from typing import List

class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        result = [[rStart, cStart]]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0
        step_size = 1
        step_count = 0
        
        while len(result) < rows * cols:
            if direction_index == 0 or direction_index == 2:
                step_size += 1
            
            for _ in range(step_size):
                rStart, cStart = rStart + directions[direction_index][0], cStart + directions[direction_index][1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
            
            direction_index = (direction_index + 1) % 4
            step_count += 1
        
        return result
