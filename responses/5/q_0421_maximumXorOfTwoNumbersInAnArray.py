class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        nums = [[(num >> i) & 1 for i in range(L)][::-1] for num in nums]
        root = TrieNode()
        ans = 0

        for num in nums:
            node = root
            xor_node = root
            curr_xor = 0

            for bit in num:
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

                toggled_bit = 1 - bit
                if toggled_bit in xor_node.children:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node.children[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node.children[bit]
            
            ans = max(ans, curr_xor)

        return ans