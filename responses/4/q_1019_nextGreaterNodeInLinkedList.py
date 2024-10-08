class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []  # Initialize a stack to keep track of elements
        result = []  # Initialize a result list to store the next greater elements

        # Iterate through the linked list to find the next greater node
        while head:
            while stack and stack[-1][1] < head.val:
                _, val = stack.pop()
                result[val] = head.val
            stack.append((len(result), head.val))
            result.append(0)
            head = head.next

        return result
