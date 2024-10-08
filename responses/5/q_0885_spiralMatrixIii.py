class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        res = [(rStart, cStart)]
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        cnt, step = 0, 1
        while len(res) < rows * cols:
            for _ in range(2):
                dr, dc = move[cnt % 4]
                for _ in range(step):
                    rStart, cStart = rStart + dr, cStart + dc
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                cnt += 1
            step += 1
        return res