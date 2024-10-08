from collections import Counter

class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        items = sorted(zip(values, labels), reverse=True)
        label_counter = Counter()
        score = 0
        num_selected = 0
        
        for value, label in items:
            if num_selected == numWanted:
                break
            
            if label_counter[label] < useLimit:
                score += value
                label_counter[label] += 1
                num_selected += 1
        
        return score
