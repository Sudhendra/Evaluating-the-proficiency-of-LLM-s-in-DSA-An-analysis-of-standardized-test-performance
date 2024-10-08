from typing import List

class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        result = [[rStart, cStart]]
        steps = 1
        while len(result) < rows * cols:
            for _ in range(steps):
                cStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])

            for _ in range(steps):
                rStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])

            steps += 1

            for _ in range(steps):
                cStart -= 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])

            for _ in range(steps):
                rStart -= 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])

            steps += 1

        return result
