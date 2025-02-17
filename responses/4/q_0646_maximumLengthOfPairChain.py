from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        end = float('-inf')
        longest_chain = 0
        for pair in pairs:
            if pair[0] > end:
                longest_chain += 1
                end = pair[1]
        return longest_chain
