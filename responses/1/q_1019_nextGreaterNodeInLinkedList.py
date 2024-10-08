class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []

        stack = []
        result = []
        index = 0
        while head:
            result.append(0)
            while stack and stack[-1][0] < head.val:
                i = stack.pop()[1]
                result[i] = head.val
            stack.append((head.val, index))
            head = head.next
            index += 1

        return result