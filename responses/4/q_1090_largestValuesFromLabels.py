from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        value_label_pairs = sorted(zip(values, labels), reverse=True)
        label_count = defaultdict(int)
        max_score = 0
        count = 0

        for value, label in value_label_pairs:
            if label_count[label] < useLimit:
                max_score += value
                label_count[label] += 1
                count += 1

            if count == numWanted:
                break

        return max_score
