from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Reversing the arrays for easier manipulation from right to left
        arr1.reverse()
        arr2.reverse()
        
        # Padding the arrays with extra zeros of length 2 to handle carry
        arr1 += [0, 0]
        arr2 += [0, 0]
        
        result = []
        carry = 0
        
        for a, b in zip(arr1, arr2):
            sum_bits = a + b + carry
            result.append(sum_bits & 1)
            carry = -(sum_bits >> 1)
        
        # Removing leading zeros except for the last zero if present
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        result.reverse()
        return result
