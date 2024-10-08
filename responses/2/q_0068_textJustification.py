from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        
        while i < len(words):
            line = []
            line_length = 0
            while i < len(words) and line_length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_length += len(words[i])
                i += 1
            
            spaces = maxWidth - line_length
            num_words = len(line)
            if num_words == 1 or i == len(words):  # left justify for last line or single word line
                result.append(' '.join(line) + ' ' * (spaces - num_words + 1))
            else:
                avg_space, extra_space = divmod(spaces, num_words - 1)
                line_str = line[0]
                for j in range(1, num_words):
                    line_str += ' ' * avg_space
                    if j <= extra_space:
                        line_str += ' '
                    line_str += line[j]
                
                result.append(line_str)
        
        return result
