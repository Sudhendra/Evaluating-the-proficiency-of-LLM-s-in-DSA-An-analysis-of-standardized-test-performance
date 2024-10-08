from typing import List
from collections import Counter

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        label_count = Counter()
        total_score = 0
        selected_items = 0

        for value, label in items:
            if selected_items == numWanted:
                break
            if label_count[label] < useLimit:
                total_score += value
                selected_items += 1
                label_count[label] += 1

        return total_score
