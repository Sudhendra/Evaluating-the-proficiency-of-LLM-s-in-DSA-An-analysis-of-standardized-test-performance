class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd_head = head
        even_head = head.next
        even_node = even_head
        
        while even_node and even_node.next:
            odd_node = even_node.next
            even_node.next = odd_node.next
            odd_node.next = even_head
            odd_head.next = odd_node
            odd_head = odd_node
            even_node = even_node.next
        
        return head
