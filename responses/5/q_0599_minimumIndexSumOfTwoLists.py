from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_map = {}
        for i, restaurant in enumerate(list1):
            if restaurant in list2:
                common_map[restaurant] = i + list2.index(restaurant)

        min_index_sum = min(common_map.values())
        return [restaurant for restaurant, index_sum in common_map.items() if index_sum == min_index_sum]
