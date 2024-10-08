from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        label_val_pairs = defaultdict(list)
        for val, label in zip(values, labels):
            label_val_pairs[label].append(val)

        result = 0
        selected = defaultdict(int)
        sorted_label_val_pairs = sorted(label_val_pairs.items(), reverse=True, key=lambda x: sum(x[1]))

        for label_vals in sorted_label_val_pairs:
            label, vals = label_vals
            vals.sort(reverse=True)

            for val in vals:
                if selected[label] < useLimit and numWanted > 0:
                    result += val
                    selected[label] += 1
                    numWanted -= 1

        return result