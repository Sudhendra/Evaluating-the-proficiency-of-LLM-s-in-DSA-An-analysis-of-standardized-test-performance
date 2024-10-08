from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        
        for node in lists:
            while node:
                pq.put(node.val)
                node = node.next
        
        dummy = ListNode(0)
        cur = dummy
        while not pq.empty():
            cur.next = ListNode(pq.get())
            cur = cur.next
        
        return dummy.next
