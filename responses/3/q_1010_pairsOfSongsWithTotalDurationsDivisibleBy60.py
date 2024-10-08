from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count_remainder = [0] * 60
        pair_count = 0

        for t in time:
            if t % 60 == 0:
                pair_count += count_remainder[0]
            else:
                pair_count += count_remainder[60 - t % 60]

            count_remainder[t % 60] += 1

        return pair_count
