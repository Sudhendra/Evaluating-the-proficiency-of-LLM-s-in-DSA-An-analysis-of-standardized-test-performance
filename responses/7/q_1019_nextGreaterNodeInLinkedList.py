from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        result = []
        
        # Convert linked list to a list
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        
        for i, val in enumerate(vals):
            while stack and val > vals[stack[-1]]:
                result[stack.pop()] = val
            stack.append(i)
            result.append(0)
        
        return result
