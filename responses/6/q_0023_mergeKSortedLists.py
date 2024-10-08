from queue import PriorityQueue

class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        q = PriorityQueue()

        for i, node in enumerate(lists):
            if node:
                q.put((node.val, i, node))

        while not q.empty():
            val, i, node = q.get()
            current.next = ListNode(val)
            current = current.next

            if node.next:
                q.put((node.next.val, i, node.next))

        return dummy.next
