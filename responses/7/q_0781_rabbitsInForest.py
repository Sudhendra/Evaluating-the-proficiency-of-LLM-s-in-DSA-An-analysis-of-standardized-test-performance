from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0
        
        for answer, freq in count.items():
            groups = freq // (answer + 1)
            if freq % (answer + 1) != 0:
                groups += 1
            total_rabbits += groups * (answer + 1)
        
        return total_rabbits
