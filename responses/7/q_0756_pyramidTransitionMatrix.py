from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def buildPyramid(cur, above, idx):
            if len(cur) == 1 and len(above) == 1:
                return True
            if idx == len(cur) - 1:
                return buildPyramid(above, "", 0)
            for triplet in allowed:
                a, b, c = triplet
                if cur[idx] + cur[idx+1] == a + b:
                    if buildPyramid(cur, above + c, idx + 1):
                        return True
            return False

        blocks = defaultdict(list)
        for triplet in allowed:
            blocks[triplet[:2]].append(triplet[2])

        def generateNextRow(row):
            if len(row) == 1:
                return [row]
            return [blocks[row[i:i+2]] for i in range(len(row)-1)]

        rows = [bottom]
        while len(rows[-1]) > 1:
            next_row = []
            for block in generateNextRow(rows[-1]):
                next_row.extend(block)
            rows.append(''.join(next_row))

        return buildPyramid(rows[-1], "", 0)
