from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        remainders = [0] * 60
        
        for t in time:
            required_remainder = (60 - t % 60) % 60
            count += remainders[required_remainder]
            remainders[t % 60] += 1
            
        return count
