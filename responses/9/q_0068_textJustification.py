from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)
        
        while i < n:
            line = []
            line_len = 0
            
            # Get words for one line
            while i < n and line_len + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i])
                i += 1
                
            # If it's the last line or only 1 word in line
            if i == n or len(line) == 1:
                result.append(" ".join(line).ljust(maxWidth))
            else:
                spaces = maxWidth - line_len
                gaps = len(line) - 1
                avg_spaces = spaces // gaps
                extra_spaces = spaces % gaps
                
                justified_line = line[0]
                for j in range(1, len(line)):
                    justified_line += ' ' * avg_spaces
                    if j <= extra_spaces:
                        justified_line += ' '
                    justified_line += line[j]
                
                result.append(justified_line)
        
        return result
