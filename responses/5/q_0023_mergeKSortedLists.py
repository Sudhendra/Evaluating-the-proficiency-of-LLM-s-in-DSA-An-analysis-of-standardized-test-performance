from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        pq = PriorityQueue()

        for node in lists:
            if node:
                pq.put((node.val, node))

        while not pq.empty():
            val, node = pq.get()
            current.next = ListNode(val)
            current = current.next
            node = node.next
            if node:
                pq.put((node.val, node))

        return head.next
