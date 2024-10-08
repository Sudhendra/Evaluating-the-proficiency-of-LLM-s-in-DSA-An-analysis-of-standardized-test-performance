from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer_count = {}
        for answer in answers:
            if answer not in answer_count:
                answer_count[answer] = 1
            else:
                answer_count[answer] += 1
        
        min_rabbits = 0
        for k, v in answer_count.items():
            group_size = k + 1
            groups = v // group_size
            remaining = v % group_size
            min_rabbits += groups * group_size
            if remaining > 0:
                min_rabbits += group_size
        
        return min_rabbits
