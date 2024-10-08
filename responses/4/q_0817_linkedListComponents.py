class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        connected_components = 0
        connected = False

        while head:
            if head.val in num_set:
                connected = True
            elif connected:
                connected_components += 1
                connected = False

            head = head.next

        if connected:
            connected_components += 1

        return connected_components
