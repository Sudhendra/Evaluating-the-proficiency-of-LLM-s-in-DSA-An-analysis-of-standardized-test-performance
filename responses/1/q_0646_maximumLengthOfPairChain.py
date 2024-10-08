from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')

        for pair in pairs:
            if pair[0] > end:
                count += 1
                end = pair[1]

        return count
