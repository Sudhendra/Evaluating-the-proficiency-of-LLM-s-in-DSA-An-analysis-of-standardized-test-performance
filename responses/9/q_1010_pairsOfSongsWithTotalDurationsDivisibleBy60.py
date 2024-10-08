from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        result = 0

        for t in time:
            complement = (60 - t % 60) % 60
            result += count[complement]
            count[t % 60] += 1

        return result
