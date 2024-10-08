class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for linked_list in lists:
            while linked_list:
                nodes.append(linked_list.val)
                linked_list = linked_list.next
        nodes.sort()
        dummy = ListNode(0)
        current = dummy
        for val in nodes:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
