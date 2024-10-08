from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {char: idx for idx, char in enumerate(s)}

        result = []
        start = 0
        end = 0

        for idx, char in enumerate(s):
            end = max(end, last_index[char])

            if idx == end:
                result.append(end - start + 1)
                start = idx + 1

        return result