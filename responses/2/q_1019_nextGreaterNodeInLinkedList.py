class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []

        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        stack = []
        result = [0] * len(vals)

        for i, val in enumerate(vals):
            while stack and vals[stack[-1]] < val:
                result[stack.pop()] = val
            stack.append(i)

        return result
