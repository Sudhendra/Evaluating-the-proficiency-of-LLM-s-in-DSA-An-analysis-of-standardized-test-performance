from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def buildPyramid(row, next_row, idx = 0, tmp = []):
            if len(row) == 1:
                return True
            if idx == len(row) - 1:
                return buildPyramid(next_row, "", 0, tmp)
            
            for rule in allowed:
                if row[idx:idx+2] in rule[:2]:
                    for ch in rule[2]:
                        if buildPyramid(row, next_row + ch, idx+1, tmp):
                            return True
            return False
        
        return buildPyramid(bottom, "")
