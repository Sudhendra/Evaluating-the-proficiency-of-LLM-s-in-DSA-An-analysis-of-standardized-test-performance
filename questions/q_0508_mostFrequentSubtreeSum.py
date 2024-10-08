front_matter = {
    "qid": 508,
    "title": "Most Frequent Subtree Sum",
    "titleSlug": "most-frequent-subtree-sum",
    "difficulty": "Medium",
    "tags": ["Hash Table", "Tree", "Depth-First Search", "Binary Tree"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Given the `root` of a binary tree, return the most frequent **subtree sum**. If there is a tie, return all the values with the highest frequency in any order.

    The **subtree sum** of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg)
    ```
    Input: root = [5,2,-3]
    Output: [2,-3,4]
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg)
    ```
    Input: root = [5,2,-5]
    Output: [2]
    ```


    **Constraints:**

    * The number of nodes in the tree is in the range `[1, 10^{4}]`.
    * `-10^{5} <= Node.val <= 10^{5}`
    """

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
