from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        
        target_sum = total_sum // 3
        part_sum = 0
        count = 0
        
        for num in arr:
            part_sum += num
            if part_sum == target_sum:
                count += 1
                part_sum = 0
                
        return count >= 3
