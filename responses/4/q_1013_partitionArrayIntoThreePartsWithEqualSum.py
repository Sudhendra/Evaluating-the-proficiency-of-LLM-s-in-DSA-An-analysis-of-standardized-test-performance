from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        
        target_sum = total_sum // 3
        prefix_sum = 0
        count = 0
        
        for num in arr:
            prefix_sum += num
            if prefix_sum == target_sum:
                count += 1
                prefix_sum = 0
                
            if count == 3:
                return True
        
        return False
