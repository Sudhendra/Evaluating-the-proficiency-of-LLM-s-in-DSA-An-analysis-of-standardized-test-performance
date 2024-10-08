from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        remainders = [0] * 60

        for t in time:
            if t % 60 == 0:
                count += remainders[0]
            else:
                count += remainders[60 - t % 60]
            remainders[t % 60] += 1

        return count
