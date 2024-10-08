class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0

        for char in s:
            char_width = widths[ord(char) - ord('a')]
            if width + char_width > 100:
                lines += 1
                width = char_width
            else:
                width += char_width

        return [lines, width]