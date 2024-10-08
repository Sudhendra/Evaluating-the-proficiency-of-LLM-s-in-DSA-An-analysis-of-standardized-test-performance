class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)  # Convert nums list to a set for faster lookup
        current = head
        connected = False
        count = 0

        while current:
            if current.val in num_set:
                connected = True
            elif connected:
                count += 1
                connected = False

            current = current.next

        if connected:
            count += 1  # If the last node was part of a component, increment count
        
        return count
