from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        MAX_BIT = 30
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        maxXOR = 0
        for num in nums:
            xorResult = 0
            node = root
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                if (1 - bit) in node.children:
                    xorResult += (1 << i)
                    node = node.children[1 - bit]
                else:
                    node = node.children[bit]
            maxXOR = max(maxXOR, xorResult)
        
        return maxXOR
