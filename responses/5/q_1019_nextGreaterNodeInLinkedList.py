from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        stack = []
        result = [0] * len(values)

        for i in range(len(values)):
            while stack and values[stack[-1]] < values[i]:
                result[stack.pop()] = values[i]
            stack.append(i)

        return result
