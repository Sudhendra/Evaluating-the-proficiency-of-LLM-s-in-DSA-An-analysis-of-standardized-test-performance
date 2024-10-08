from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort pairs based on the end value
        count = 0
        end = float('-inf')
        
        for pair in pairs:
            if pair[0] > end:  # If the start value of current pair is greater than the end value of the previous pair
                count += 1
                end = pair[1]  # Update the end value
        return count
