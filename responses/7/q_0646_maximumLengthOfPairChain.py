from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort pairs by the ending value
        prev_end, chain_length = float('-inf'), 0
        for pair in pairs:
            if prev_end < pair[0]:  # If the current pair can be added to the chain
                prev_end = pair[1]
                chain_length += 1
        return chain_length
