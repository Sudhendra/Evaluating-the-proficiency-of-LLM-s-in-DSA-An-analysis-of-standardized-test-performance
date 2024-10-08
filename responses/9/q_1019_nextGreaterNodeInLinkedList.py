class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        n = len(arr)
        stack, res = [], [0]*n
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                res[stack.pop()] = arr[i]
            stack.append(i)
        
        return res
