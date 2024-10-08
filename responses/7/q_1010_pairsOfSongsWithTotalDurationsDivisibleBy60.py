class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        remainder_count = [0] * 60
        
        for t in time:
            count += remainder_count[-t % 60]
            remainder_count[t % 60] += 1
        
        return count