from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        pq = PriorityQueue()
        dummy = ListNode(0)
        tail = dummy
        
        for node in lists:
            if node:
                pq.put((node.val, node))
        
        while not pq.empty():
            val, node = pq.get()
            tail.next = node
            tail = tail.next
            if node.next:
                pq.put((node.next.val, node.next))
        
        return dummy.next
