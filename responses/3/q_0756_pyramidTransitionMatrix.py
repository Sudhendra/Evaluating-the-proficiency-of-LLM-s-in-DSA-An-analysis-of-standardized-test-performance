from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def build_pyramid(level, curr_row, next_row, allowed_set):
            if level == len(bottom) - 1:
                return True

            if len(next_row) == len(curr_row) - 1:
                return build_pyramid(level + 1, next_row, "", allowed_set)

            pos = len(next_row)
            base = curr_row[pos:pos+2]
            for option in allowed_set:
                if option[:2] == base:
                    if build_pyramid(level, curr_row, next_row + option[2], allowed_set):
                        return True
            
            return False

        allowed_set = set(allowed)
        return build_pyramid(0, bottom, "", allowed_set)
