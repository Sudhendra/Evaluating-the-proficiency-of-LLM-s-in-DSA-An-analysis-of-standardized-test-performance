from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def subtree_sum(node):
            if not node:
                return 0
            s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            counter[s] += 1
            return s
        
        if not root:
            return []
        
        counter = Counter()
        subtree_sum(root)
        
        max_freq = max(counter.values())
        return [sum_value for sum_value, freq in counter.items() if freq == max_freq]
