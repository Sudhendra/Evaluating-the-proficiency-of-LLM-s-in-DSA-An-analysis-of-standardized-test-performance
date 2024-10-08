class Solution:
    
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen_remainders = {0: -1}  # Storing the remainder and its index
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            if k != 0:
                running_sum %= k
            
            if running_sum in seen_remainders:
                if i - seen_remainders[running_sum] > 1:
                    return True
            else:
                seen_remainders[running_sum] = i
        
        return False
