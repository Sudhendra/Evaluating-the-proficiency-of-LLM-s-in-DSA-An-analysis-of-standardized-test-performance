from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def subtree_sum(node):
            if not node:
                return 0
            s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            sums.append(s)
            return s
        
        sums = []
        subtree_sum(root)
        count = Counter(sums)
        max_freq = max(count.values())
        return [s for s in count if count[s] == max_freq]
