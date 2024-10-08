from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        length = 0
        
        for word in words:
            if length + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - length):
                    line[i % (len(line) - 1 or 1)] += ' '
                result.append(''.join(line))
                line = []
                length = 0
            line.append(word)
            length += len(word)
        
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
