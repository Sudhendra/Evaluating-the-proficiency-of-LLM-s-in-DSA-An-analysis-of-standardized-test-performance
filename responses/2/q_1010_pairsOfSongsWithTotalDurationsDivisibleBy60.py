from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        remainder_map = defaultdict(int)
        for t in time:
            if t % 60 == 0:
                count += remainder_map[0]
            else:
                count += remainder_map[60 - t % 60]
            remainder_map[t % 60] += 1
        return count
