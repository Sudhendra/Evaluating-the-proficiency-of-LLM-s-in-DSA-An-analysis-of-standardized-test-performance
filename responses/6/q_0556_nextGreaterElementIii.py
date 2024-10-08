class Solution:
    
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        
        # Step 1: Find the first decreasing digit from right to left
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i == -1:
            return -1
        
        # Step 2: Find the smallest digit on the right side of nums[i] that is greater than nums[i]
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the numbers from i+1 to the end
        nums[i+1:] = nums[i+1:][::-1]
        
        result = int(''.join(nums))
        return result if result <= 2**31 - 1 else -1
