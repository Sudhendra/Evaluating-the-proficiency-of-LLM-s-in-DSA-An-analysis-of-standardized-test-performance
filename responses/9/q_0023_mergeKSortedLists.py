from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = PriorityQueue()
        for list_node in lists:
            while list_node:
                q.put(list_node.val)
                list_node = list_node.next
        
        dummy = ListNode(0)
        curr = dummy
        while not q.empty():
            curr.next = ListNode(q.get())
            curr = curr.next
        
        return dummy.next
