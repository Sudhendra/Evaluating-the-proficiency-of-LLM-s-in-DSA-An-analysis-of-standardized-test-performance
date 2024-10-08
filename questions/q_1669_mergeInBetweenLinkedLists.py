front_matter = {
    "qid": 1669,
    "title": "Merge In Between Linked Lists",
    "titleSlug": "merge-in-between-linked-lists",
    "difficulty": "Medium",
    "tags": ["Linked List"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively.

    Remove `list1`'s nodes from the `a^{th}` node to the `b^{th}` node, and put `list2` in their place.

    The blue edges and nodes in the following figure indicate the result:

    ![](https://assets.leetcode.com/uploads/2020/11/05/fig1.png)
    *Build the result list and return its head.*



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2024/03/01/ll.png)
    ```
    Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
    Output: [10,1,13,1000000,1000001,1000002,5]
    Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex2.png)
    ```
    Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
    Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
    Explanation: The blue edges and nodes in the above figure indicate the result.
    ```


    **Constraints:**

    * `3 <= list1.length <= 10^{4}`
    * `1 <= a <= b < list1.length - 1`
    * `1 <= list2.length <= 10^{4}`
    """

    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
