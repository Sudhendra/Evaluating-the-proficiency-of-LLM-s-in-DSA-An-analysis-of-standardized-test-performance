class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        
        part_size, extra_nodes = divmod(size, k)
        result = []
        current = head
        
        for i in range(k):
            result.append(current)
            part_length = part_size + (i < extra_nodes)
            
            for _ in range(part_length-1):
                if current:
                    current = current.next
            if current:
                current.next, current = None, current.next
        
        return result
