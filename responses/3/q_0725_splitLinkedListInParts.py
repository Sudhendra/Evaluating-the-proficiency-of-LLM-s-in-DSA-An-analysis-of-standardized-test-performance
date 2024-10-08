class Solution:
    
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        n = 0
        while current:
            n += 1
            current = current.next
        
        div, rem = divmod(n, k)
        
        result = []
        current = head
        for i in range(k):
            size = div + 1 if i < rem else div
            if not size:
                result.append(None)
            else:
                result.append(current)
                for j in range(size - 1):
                    current = current.next
                current.next, current = None, current.next
        
        return result
