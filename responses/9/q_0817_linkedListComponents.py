class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        connected = False
        
        while head:
            if head.val in num_set:
                connected = True
            else:
                if connected:
                    count += 1
                    connected = False
            head = head.next
                
        if connected:
            count += 1
            
        return count
