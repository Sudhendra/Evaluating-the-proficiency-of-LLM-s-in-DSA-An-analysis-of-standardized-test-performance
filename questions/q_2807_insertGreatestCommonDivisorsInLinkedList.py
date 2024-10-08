front_matter = {
    "qid": 2807,
    "title": "Insert Greatest Common Divisors in Linked List",
    "titleSlug": "insert-greatest-common-divisors-in-linked-list",
    "difficulty": "Medium",
    "tags": ["Linked List", "Math", "Number Theory"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """Given the head of a linked list `head`, in which each node contains an integer value.

    Between every pair of adjacent nodes, insert a new node with a value equal to the **greatest common divisor** of them.

    Return *the linked list after insertion*.

    The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2023/07/18/ex1_copy.png)
    ```
    Input: head = [18,6,10,3]
    Output: [18,6,6,2,10,1,3]
    Explanation: The 1^{st} diagram denotes the initial linked list and the 2^{nd} diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
    - We insert the greatest common divisor of 18 and 6 = 6 between the 1^{st} and the 2^{nd} nodes.
    - We insert the greatest common divisor of 6 and 10 = 2 between the 2^{nd} and the 3^{rd} nodes.
    - We insert the greatest common divisor of 10 and 3 = 1 between the 3^{rd} and the 4^{th} nodes.
    There are no more adjacent nodes, so we return the linked list.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2023/07/18/ex2_copy1.png)
    ```
    Input: head = [7]
    Output: [7]
    Explanation: The 1^{st} diagram denotes the initial linked list and the 2^{nd} diagram denotes the linked list after inserting the new nodes.
    There are no pairs of adjacent nodes, so we return the initial linked list.
    ```


    **Constraints:**

    * The number of nodes in the list is in the range `[1, 5000]`.
    * `1 <= Node.val <= 1000`
    """

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
