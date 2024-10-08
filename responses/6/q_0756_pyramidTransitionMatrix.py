from collections import defaultdict
from itertools import product

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def build_pyramid(level, row):
            if len(row) == 1:
                return True

            if level == len(row) - 1:
                return build_pyramid(0, "")

            for block in blocks[(row[level], row[level + 1])]:
                if build_pyramid(level + 1, row + block):
                    return True

            return False

        blocks = defaultdict(list)
        for block in allowed:
            blocks[(block[0], block[1])].append(block[2])

        return build_pyramid(0, bottom)
