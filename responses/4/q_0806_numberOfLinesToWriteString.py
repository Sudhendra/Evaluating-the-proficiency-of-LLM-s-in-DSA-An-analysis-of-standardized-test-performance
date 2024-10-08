from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        pixels = 0
        
        for char in s:
            width = widths[ord(char) - ord('a')]
            if pixels + width > 100:
                lines += 1
                pixels = width
            else:
                pixels += width
        
        return [lines, pixels]
