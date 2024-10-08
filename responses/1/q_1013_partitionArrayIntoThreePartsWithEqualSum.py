class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        
        target = total_sum // 3
        part_sum, parts_found = 0, 0
        
        for num in arr:
            part_sum += num
            if part_sum == target:
                parts_found += 1
                part_sum = 0
                
        return parts_found >= 3
