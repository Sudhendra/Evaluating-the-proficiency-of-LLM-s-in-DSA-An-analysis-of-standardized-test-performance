class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        result = []
        part_size, remainder = divmod(length, k)
        current = head
        for i in range(k):
            part_head = ListNode(0)
            part_current = part_head
            for j in range(part_size + (i < remainder)):
                if current:
                    part_current.next = ListNode(current.val)
                    part_current = part_current.next
                    current = current.next
            result.append(part_head.next)
        
        return result
