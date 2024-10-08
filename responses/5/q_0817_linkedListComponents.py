class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        connected_components = 0
        in_component = False

        while head:
            if head.val in num_set:
                if not in_component:
                    connected_components += 1
                    in_component = True
            else:
                in_component = False

            head = head.next

        return connected_components
