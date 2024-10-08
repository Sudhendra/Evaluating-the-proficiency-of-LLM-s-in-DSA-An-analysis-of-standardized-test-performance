from typing import List

class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        dx = [0, 1, 0, -1]  # directions: right, down, left, up
        dy = [1, 0, -1, 0]
        res = [[rStart, cStart]]
        
        step = 0
        direction = 0
        x, y = rStart, cStart
        
        while len(res) < rows * cols:
            if direction % 2 == 0:  # increment step every 2 directions
                step += 1
            for _ in range(step):
                x += dx[direction]
                y += dy[direction]
                if 0 <= x < rows and 0 <= y < cols:
                    res.append([x, y])
            direction = (direction + 1) % 4
        
        return res
