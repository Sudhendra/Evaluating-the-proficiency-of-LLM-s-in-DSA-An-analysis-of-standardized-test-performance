class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        part_size = count // k
        extra = count % k

        result = []
        curr = head
        for i in range(k):
            result.append(curr)
            part_length = part_size + (1 if i < extra else 0)
            for j in range(part_length - 1):
                if curr:
                    curr = curr.next
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp

        return result
