from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        row = [1] + [0] * (rowIndex - 1) + [1]

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j-1]

        return row
