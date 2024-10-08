from typing import List

class Solution:

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        current_end = float('-inf')
        longest_chain = 0

        for pair in pairs:
            if pair[0] > current_end:
                current_end = pair[1]
                longest_chain += 1

        return longest_chain

# If you have multiple solutions, add them all here as methods of the same class.
