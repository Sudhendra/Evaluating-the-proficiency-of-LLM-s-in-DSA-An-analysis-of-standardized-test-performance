from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def subtree_sum(node, sums):
            if not node:
                return 0

            current_sum = node.val + subtree_sum(node.left, sums) + subtree_sum(node.right, sums)
            sums[current_sum] += 1

            return current_sum

        if not root:
            return []

        sums = Counter()
        subtree_sum(root, sums)
        max_freq = max(sums.values())
        
        return [s for s in sums if sums[s] == max_freq]
