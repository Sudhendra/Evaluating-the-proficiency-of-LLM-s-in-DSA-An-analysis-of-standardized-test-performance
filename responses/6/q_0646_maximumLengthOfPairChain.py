from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        current_end = float('-inf')
        count = 0
        for pair in pairs:
            if pair[0] > current_end:
                count += 1
                current_end = pair[1]
        return count
