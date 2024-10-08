class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        components = 0
        num_set = set(nums)
        current = head
        connected = False

        while current:
            if current.val in num_set:
                if not connected:
                    components += 1
                    connected = True
            else:
                connected = False
            current = current.next
        
        return components