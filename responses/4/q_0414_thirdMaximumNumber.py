from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float('-inf')

        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif first_max > num > second_max:
                third_max = second_max
                second_max = num
            elif second_max > num > third_max:
                third_max = num

        if third_max != float('-inf'):
            return third_max
        else:
            return first_max
