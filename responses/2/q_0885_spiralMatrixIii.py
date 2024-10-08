from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        direction = 0
        r, c = rStart, cStart
        while len(res) < rows * cols:
            if 0 <= r < rows and 0 <= c < cols:
                res.append([r, c])
            for _ in range(steps):
                r, c = r + directions[direction][0], c + directions[direction][1]
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            direction = (direction + 1) % 4
            if direction % 2 == 0:
                steps += 1
        return res
