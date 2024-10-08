class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        part_size, extra_nodes = divmod(length, k)
        
        result = []
        curr = head
        for i in range(k):
            result.append(curr)
            part_len = part_size + (i < extra_nodes)
            for _ in range(part_len-1):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None, curr.next

        return result
