from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_nums = [num for num in nums if num % 2 == 0]
        odd_nums = [num for num in nums if num % 2 != 0]
        return even_nums + odd_nums
