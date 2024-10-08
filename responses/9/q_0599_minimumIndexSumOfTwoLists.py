from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = float('inf')
        common_strings = []

        hashmap = {s: i for i, s in enumerate(list1)}
        
        for j, s in enumerate(list2):
            if s in hashmap:
                curr_sum = j + hashmap[s]
                if curr_sum < index_sum:
                    index_sum = curr_sum
                    common_strings = [s]
                elif curr_sum == index_sum:
                    common_strings.append(s)

        return common_strings
