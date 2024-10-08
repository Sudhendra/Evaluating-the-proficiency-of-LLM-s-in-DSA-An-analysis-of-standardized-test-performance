from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        carry = 0
        result = []
        
        while arr1 or arr2 or carry:
            if arr1:
                carry += arr1.pop()
            if arr2:
                carry += arr2.pop()
                
            result.append(carry & 1)
            carry = -(carry >> 1)
        
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return result[::-1]
