from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        for ans in answers:
            count[ans] = count.get(ans, 0) + 1
        result = 0
        for ans, cnt in count.items():
            result += ((cnt + ans) // (ans + 1)) * (ans + 1)
        return result
