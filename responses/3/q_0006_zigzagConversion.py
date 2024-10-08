class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = ['' for _ in range(numRows)]
        
        direction = 1
        cur_row = 0
        
        for char in s:
            rows[cur_row] += char
            cur_row += direction
            
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1
        
        return ''.join(rows)