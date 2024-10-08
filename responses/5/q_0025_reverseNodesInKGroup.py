# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while head:
            group_start = head
            length = getLength(group_start)
            
            if length < k:
                break
                
            group_end = head
            for _ in range(k - 1):
                group_end = group_end.next
            
            next_group_start = group_end.next
            
            new_head = reverseLinkedList(group_start, k)
            prev_group_end.next = new_head
            group_start.next = next_group_start
            
            prev_group_end = group_start
            head = next_group_start
        
        return dummy.next
