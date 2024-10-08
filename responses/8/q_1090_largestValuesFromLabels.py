class Solution:
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        items = sorted(zip(values, labels), reverse=True)
        label_count = {}
        total_score = 0

        for value, label in items:
            if numWanted == 0:
                break

            if label_count.get(label, 0) < useLimit:
                total_score += value
                label_count[label] = label_count.get(label, 0) + 1
                numWanted -= 1

        return total_score
