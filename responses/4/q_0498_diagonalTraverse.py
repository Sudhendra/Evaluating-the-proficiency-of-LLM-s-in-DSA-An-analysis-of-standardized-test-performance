from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for i in range(m + n - 1):
            if i % 2 == 0:
                r, c = min(i, m - 1), max(0, i - m + 1)
                while r >= max(0, i - n + 1) and c <= min(i, n - 1):
                    result.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                r, c = max(0, i - n + 1), min(i, n - 1)
                while r <= min(i, m - 1) and c >= max(0, i - m + 1):
                    result.append(mat[r][c])
                    r += 1
                    c -= 1

        return result
