from collections import Counter
from typing import List

class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        value_label_pairs = sorted(zip(values, labels), reverse=True)
        label_count = Counter()
        score = 0
        selected_items = 0

        for value, label in value_label_pairs:
            if selected_items == numWanted:
                break
            if label_count[label] < useLimit:
                score += value
                label_count[label] += 1
                selected_items += 1

        return score
