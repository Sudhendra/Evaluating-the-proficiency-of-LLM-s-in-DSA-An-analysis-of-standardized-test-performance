from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_result = 0
        for num in nums:
            xor_result ^= num

        diff_bit = 1
        while (diff_bit & xor_result) == 0:
            diff_bit <<= 1

        num1, num2 = 0, 0
        for num in nums:
            if (num & diff_bit) == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
