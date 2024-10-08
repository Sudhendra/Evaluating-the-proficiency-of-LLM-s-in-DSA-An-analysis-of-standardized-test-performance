class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = [''] * numRows
        idx, step = 0, 1

        for char in s:
            res[idx] += char

            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1

            idx += step

        return ''.join(res)
