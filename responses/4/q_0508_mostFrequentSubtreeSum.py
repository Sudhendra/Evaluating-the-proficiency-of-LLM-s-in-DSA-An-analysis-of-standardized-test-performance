from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def subtree_sum(node, freq):
            if not node:
                return 0
            cur_sum = node.val + subtree_sum(node.left, freq) + subtree_sum(node.right, freq)
            freq[cur_sum] += 1
            return cur_sum

        if not root:
            return []

        freq = Counter()
        subtree_sum(root, freq)
        max_freq = max(freq.values())

        return [key for key, value in freq.items() if value == max_freq]
