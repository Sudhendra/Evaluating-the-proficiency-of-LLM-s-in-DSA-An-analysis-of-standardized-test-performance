front_matter = {
    "qid": 25,
    "title": "Reverse Nodes in k-Group",
    "titleSlug": "reverse-nodes-in-k-group",
    "difficulty": "Hard",
    "tags": ["Linked List", "Recursion"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.

    `k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)
    ```
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)
    ```
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
    ```


    **Constraints:**

    * The number of nodes in the list is `n`.
    * `1 <= k <= n <= 5000`
    * `0 <= Node.val <= 1000`



    **Follow-up:** Can you solve the problem in `O(1)` extra memory space?
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
