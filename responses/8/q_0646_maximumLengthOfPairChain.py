from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort pairs based on the second element
        curr_end = float('-inf')
        max_chain_len = 0
        for pair in pairs:
            if pair[0] > curr_end:
                curr_end = pair[1]
                max_chain_len += 1
        return max_chain_len
