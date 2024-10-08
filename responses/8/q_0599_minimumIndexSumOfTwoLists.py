from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        if not common:
            return []

        min_sum = float('inf')
        result = []
        for word in common:
            sum_index = list1.index(word) + list2.index(word)
            if sum_index < min_sum:
                min_sum = sum_index
                result = [word]
            elif sum_index == min_sum:
                result.append(word)

        return result
