class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        part_size, extra_nodes = divmod(length, k)
        result = []
        current = head

        for _ in range(k):
            part_head = current
            for _ in range(part_size + (extra_nodes > 0) - 1):
                if current:
                    current = current.next
            if current:
                current.next, current = None, current.next

            result.append(part_head)
            extra_nodes -= 1

        return result
