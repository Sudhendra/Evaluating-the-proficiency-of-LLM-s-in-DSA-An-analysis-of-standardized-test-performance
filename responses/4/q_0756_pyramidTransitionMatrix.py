from collections import defaultdict
from itertools import product

class Solution:
    
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def can_build(pyramid, level, row, next_row):
            if len(row) == 1:
                pyramid.append(row)
                if len(row[0]) == 1:
                    return True
                return can_build(pyramid, level + 1, next_row, [])
            
            for possible_blocks in product(*(allowed_dict[left + right] for left, right in zip(row[:-1], row[1:]))):
                if can_build(pyramid, level, row[1:], next_row + [possible_blocks]):
                    return True
            
            return False
        
        allowed_dict = defaultdict(list)
        for pattern in allowed:
            allowed_dict[pattern[:2]].append(pattern[2])
        
        pyramid = []
        return can_build(pyramid, 0, list(bottom), [])
