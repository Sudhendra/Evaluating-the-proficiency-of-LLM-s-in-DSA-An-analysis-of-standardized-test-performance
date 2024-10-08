from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def subtree_sum(node):
            if not node:
                return 0
            s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            count[s] += 1
            return s
        
        count = Counter()
        subtree_sum(root)
        max_freq = max(count.values() or [0])
        return [s for s, freq in count.items() if freq == max_freq]
