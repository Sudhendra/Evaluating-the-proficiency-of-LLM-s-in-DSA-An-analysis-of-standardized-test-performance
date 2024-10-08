from collections import Counter

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        label_count, score, res = Counter(), 0, 0
        
        for value, label in items:
            if label_count[label] < useLimit:
                res += value
                label_count[label] += 1
                numWanted -= 1
                score += value
                if numWanted == 0:
                    break
        
        return score
