from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        rabbits = 0
        for ans in answers:
            if ans not in count:
                count[ans] = 0
            count[ans] += 1
        
        for key in count:
            group_size = key + 1
            groups = count[key] // group_size
            if count[key] % group_size != 0:
                groups += 1
            rabbits += groups * group_size
        
        return rabbits