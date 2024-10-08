class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        while i < len(words):
            line = []
            length = 0
            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
                
            spaces = maxWidth - length
            if len(line) == 1 or i == len(words):
                result.append(" ".join(line) + " " * (spaces - len(line) + 1))
            else:
                num_gaps = len(line) - 1
                space_between_words = spaces // num_gaps
                extra_spaces = spaces % num_gaps
                justified_line = ''
                for j in range(len(line) - 1):
                    justified_line += line[j] + " " * (space_between_words + (1 if j < extra_spaces else 0))
                justified_line += line[-1]
                result.append(justified_line)
        
        return result
