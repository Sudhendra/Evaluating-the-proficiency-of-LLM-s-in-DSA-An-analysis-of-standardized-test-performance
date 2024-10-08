def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    result = []
    stack = []
    index_stack = []
    index = 0
    while head:
        while stack and head.val > stack[-1]:
            result[index_stack.pop()] = head.val
            stack.pop()
        result.append(0)
        stack.append(head.val)
        index_stack.append(index)
        index += 1
        head = head.next
    return result
