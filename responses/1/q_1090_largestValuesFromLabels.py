from collections import defaultdict

class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        items = sorted(zip(values, labels), reverse=True)
        label_count = defaultdict(int)
        result = 0
        num_selected = 0

        for value, label in items:
            if num_selected == numWanted:
                break
            if label_count[label] < useLimit:
                result += value
                label_count[label] += 1
                num_selected += 1

        return result
