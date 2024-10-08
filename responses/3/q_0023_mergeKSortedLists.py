class Solution:
     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        
        # Custom comparison function to compare nodes based on their values
        def compare(node1, node2):
            return node1.val - node2.val
        
        # Create a min heap and push the head of each linked list into the heap
        min_heap = []
        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, l))
        
        # Create a dummy node to build the merged linked list
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            value, node = heapq.heappop(min_heap)
            # If the popped node has a next node, push it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
            # Append the popped node to the merged linked list
            curr.next = node
            curr = curr.next
        
        return dummy.next
