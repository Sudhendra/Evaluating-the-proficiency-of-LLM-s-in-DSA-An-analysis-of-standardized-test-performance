class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = list(zip(values, labels))
        items.sort(reverse=True)  # Sort items from high to low value

        label_count = defaultdict(int)
        score = 0
        selected = 0

        for value, label in items:
            if label_count[label] < useLimit:
                score += value
                selected += 1
                label_count[label] += 1

            if selected == numWanted:
                break

        return score