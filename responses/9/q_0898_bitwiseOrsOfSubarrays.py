from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        unique_bitwise_or = set()
        current = set()
        previous = set()
        
        for num in arr:
            current = {num | val for val in current} | {num}
            unique_bitwise_or |= current
            previous = current
        
        return len(unique_bitwise_or)
