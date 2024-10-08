class Solution:
    
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        components = 0
        num_set = set(nums)
        connected = False
        
        while head:
            if head.val in num_set:
                connected = True
            else:
                if connected:
                    components += 1
                connected = False
            head = head.next
        
        if connected:
            components += 1
        
        return components