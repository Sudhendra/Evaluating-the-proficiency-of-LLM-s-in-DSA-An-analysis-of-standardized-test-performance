from typing import List

class Solution:

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = {}
        result = []
        min_sum = float('inf')

        for i in range(len(list1)):
            if list1[i] in list2:
                index_sum[list1[i]] = i + list2.index(list1[i])

        for key, value in index_sum.items():
            if value < min_sum:
                min_sum = value
                result = [key]
            elif value == min_sum:
                result.append(key)

        return result
