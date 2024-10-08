class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next

        width, remainder = divmod(n, k)
        
        result = []
        cur = head
        for i in range(k):
            result.append(cur)
            size = width + (i < remainder)
            for _ in range(size - 1):
                if cur:
                    cur = cur.next
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp

        return result
