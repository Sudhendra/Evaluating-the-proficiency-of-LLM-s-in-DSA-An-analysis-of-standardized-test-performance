from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def get_subtree_sum(node):
            if not node:
                return 0
            
            subtree_sum = node.val + get_subtree_sum(node.left) + get_subtree_sum(node.right)
            subtree_sums.append(subtree_sum)
            
            return subtree_sum
        
        if not root:
            return []
        
        subtree_sums = []
        get_subtree_sum(root)
        
        freq_map = Counter(subtree_sums)
        max_freq = max(freq_map.values())
        
        return [key for key, value in freq_map.items() if value == max_freq]
