from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        unique_or_values = set()
        cur_or_values = set()
        for num in arr:
            new_or_values = {num}
            for prev_num in cur_or_values:
                new_or_values.add(prev_num | num)
            cur_or_values = new_or_values
            unique_or_values |= cur_or_values
        return len(unique_or_values)
