from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {word: i for i, word in enumerate(list1)}
        map2 = {word: i for i, word in enumerate(list2)}
        
        common_words = set(list1) & set(list2)
        min_index_sum = float('inf')
        result = []
        
        for word in common_words:
            index_sum = map1[word] + map2[word]
            if index_sum < min_index_sum:
                min_index_sum = index_sum
                result = [word]
            elif index_sum == min_index_sum:
                result.append(word)
        
        return result
