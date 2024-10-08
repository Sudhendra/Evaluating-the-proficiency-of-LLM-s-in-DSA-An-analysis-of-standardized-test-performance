from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = {}
        min_sum = float('inf')
        common_strings = []
        
        for i, restaurant in enumerate(list1):
            index_sum[restaurant] = i
            
        for j, restaurant in enumerate(list2):
            if restaurant in index_sum:
                curr_sum = index_sum[restaurant] + j
                if curr_sum < min_sum:
                    common_strings = [restaurant]
                    min_sum = curr_sum
                elif curr_sum == min_sum:
                    common_strings.append(restaurant)
        
        return common_strings
