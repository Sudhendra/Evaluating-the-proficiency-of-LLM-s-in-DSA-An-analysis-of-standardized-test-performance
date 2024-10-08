from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        cur_width = 0

        for char in s:
            char_width = widths[ord(char) - ord('a')]
            if cur_width + char_width > 100:
                lines += 1
                cur_width = char_width
            else:
                cur_width += char_width

        return [lines, cur_width]
