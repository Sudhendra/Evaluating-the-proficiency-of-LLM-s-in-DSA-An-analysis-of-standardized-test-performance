from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = float('inf')
        common = []

        index_map = {word: idx for idx, word in enumerate(list1)}
        
        for idx, word in enumerate(list2):
            if word in index_map:
                current_sum = idx + index_map[word]
                if current_sum < index_sum:
                    common = [word]
                    index_sum = current_sum
                elif current_sum == index_sum:
                    common.append(word)
                    
        return common
