from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        res = []
        for word in words:
            same_row = True
            row_idx = -1
            for c in word:
                c = c.lower()
                if row_idx == -1:
                    for idx, row in enumerate(rows):
                        if c in row:
                            row_idx = idx
                            break
                else:
                    if c not in rows[row_idx]:
                        same_row = False
                        break
            if same_row:
                res.append(word)
        return res
