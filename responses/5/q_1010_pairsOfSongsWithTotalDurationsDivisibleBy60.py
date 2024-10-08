from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        remainder_freq = [0] * 60

        for t in time:
            remainder_freq[t % 60] += 1

        count += remainder_freq[0] * (remainder_freq[0] - 1) // 2
        count += remainder_freq[30] * (remainder_freq[30] - 1) // 2

        i, j = 1, 59
        while i < j:
            count += remainder_freq[i] * remainder_freq[j]
            i += 1
            j -= 1

        return count
