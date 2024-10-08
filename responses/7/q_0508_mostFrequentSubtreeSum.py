from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def subtree_sum(node):
            if not node:
                return 0
            current_sum = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            sums.append(current_sum)
            return current_sum
        
        sums = []
        subtree_sum(root)
        count = Counter(sums)
        max_freq = max(count.values(), default=0)
        
        return [k for k, v in count.items() if v == max_freq]
