front_matter = {
    "qid": 23,
    "title": "Merge k Sorted Lists",
    "titleSlug": "merge-k-sorted-lists",
    "difficulty": "Hard",
    "tags": [
        "Linked List",
        "Divide and Conquer",
        "Heap (Priority Queue)",
        "Merge Sort",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

    *Merge all the linked-lists into one sorted linked-list and return it.*



    **Example 1:**

    ```
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
    ```
    **Example 2:**

    ```
    Input: lists = []
    Output: []
    ```
    **Example 3:**

    ```
    Input: lists = [[]]
    Output: []
    ```


    **Constraints:**

    * `k == lists.length`
    * `0 <= k <= 10^{4}`
    * `0 <= lists[i].length <= 500`
    * `-10^{4} <= lists[i][j] <= 10^{4}`
    * `lists[i]` is sorted in **ascending order**.
    * The sum of `lists[i].length` will not exceed `10^{4}`.
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
