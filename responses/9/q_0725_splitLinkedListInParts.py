class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, current = 0, head
        while current:
            length += 1
            current = current.next

        part_size, extra = divmod(length, k)
        result = []
        current = head

        for i in range(k):
            result.append(current)
            part_length = part_size + (i < extra)
            for j in range(part_length - 1):
                if current:
                    current = current.next
            if current:
                current.next, current = None, current.next

        return result
