from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        unique_or_values = set()
        prev_values = set()

        for num in arr:
            new_values = set()
            new_values.add(num)
            for prev_num in prev_values:
                new_values.add(prev_num | num)
            prev_values = new_values.copy()
            unique_or_values |= new_values

        return len(unique_or_values)
