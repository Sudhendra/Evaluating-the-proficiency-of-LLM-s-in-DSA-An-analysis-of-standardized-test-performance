class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort the pairs based on the end value of each pair
        current_end, longest_chain = float('-inf'), 0
        for pair in pairs:
            if pair[0] > current_end:
                current_end = pair[1]
                longest_chain += 1
        return longest_chain