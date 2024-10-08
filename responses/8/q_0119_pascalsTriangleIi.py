from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev_row = [1]
        for i in range(1, rowIndex + 1):
            curr_row = [1] * (i + 1)
            for j in range(1, i):
                curr_row[j] = prev_row[j-1] + prev_row[j]
            prev_row = curr_row

        return curr_row
