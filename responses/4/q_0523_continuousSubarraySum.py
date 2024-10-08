class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        prefix_sum = 0
        seen_modulo = {0: -1}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
                
            if prefix_sum in seen_modulo:
                if i - seen_modulo[prefix_sum] > 1:
                    return True
            else:
                seen_modulo[prefix_sum] = i
        
        return False
