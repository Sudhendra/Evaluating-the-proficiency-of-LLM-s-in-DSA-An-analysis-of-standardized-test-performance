from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        for ans in answers:
            if ans not in freq:
                freq[ans] = 0
            freq[ans] += 1

        total = 0
        for key, value in freq.items():
            total += ((value // (key + 1)) + (1 if value % (key + 1) != 0 else 0)) * (key + 1)

        return total
