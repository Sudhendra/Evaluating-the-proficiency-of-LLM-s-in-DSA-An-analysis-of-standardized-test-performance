from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = float('inf')
        common_strings = []
        dict1 = {string: index for index, string in enumerate(list1)}
        
        for index, string in enumerate(list2):
            if string in dict1:
                current_index_sum = index + dict1[string]
                if current_index_sum < index_sum:
                    index_sum = current_index_sum
                    common_strings = [string]
                elif current_index_sum == index_sum:
                    common_strings.append(string)
        
        return common_strings
