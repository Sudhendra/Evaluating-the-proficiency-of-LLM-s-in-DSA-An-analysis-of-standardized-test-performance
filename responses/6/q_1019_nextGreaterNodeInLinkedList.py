from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        values = []
        result = []

        index = 0
        while head:
            values.append(head.val)
            result.append(0)

            while stack and values[stack[-1]] < head.val:
                result[stack.pop()] = head.val

            stack.append(index)
            index += 1
            head = head.next

        return result
