from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')

        def is_single_row(word):
            word_set = set(word.lower())
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                return True
            return False

        return [word for word in words if is_single_row(word)]
