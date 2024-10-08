from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def subtree_sum(node):
            if not node:
                return 0
            s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            counts[s] += 1
            return s

        counts = Counter()
        subtree_sum(root)
        max_freq = max(counts.values())

        return [s for s, freq in counts.items() if freq == max_freq]
