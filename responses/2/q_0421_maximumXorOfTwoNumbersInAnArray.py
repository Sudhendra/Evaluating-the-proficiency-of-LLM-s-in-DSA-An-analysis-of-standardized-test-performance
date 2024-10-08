class Solution:
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        result, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefixes = {num & mask for num in nums}
            possible_result = result | 1 << i
            for prefix in prefixes:
                if possible_result ^ prefix in prefixes:
                    result = possible_result
                    break
        return result
