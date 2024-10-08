from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        q = PriorityQueue()
        
        for node in lists:
            if node:
                q.put((node.val, node))
        
        while not q.empty():
            val, node = q.get()
            curr.next = ListNode(val)
            curr = curr.next
            
            node = node.next
            if node:
                q.put((node.val, node))
        
        return head.next
