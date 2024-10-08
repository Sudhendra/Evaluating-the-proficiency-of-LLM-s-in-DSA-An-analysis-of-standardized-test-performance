from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(words, maxWidth, start, end, is_last=False):
            line = ""
            words_count = end - start + 1
            if words_count == 1 or is_last:
                line = words[start]
                for i in range(start + 1, end + 1):
                    line += " " + words[i]
                spaces_left = maxWidth - len(line)
                line += " " * spaces_left
            else:
                total_word_length = 0
                for i in range(start, end+1):
                    total_word_length += len(words[i])

                total_spaces = maxWidth - total_word_length
                extra_spaces = total_spaces % (words_count - 1) if words_count > 1 else total_spaces
                spaces_per_word = total_spaces // (words_count - 1) if words_count > 1 else total_spaces

                line = words[start]
                for i in range(start+1, end+1):
                    spaces = " " * (spaces_per_word + (1 if extra_spaces > 0 else 0))
                    line += spaces + words[i]
                    extra_spaces -= 1

            return line

        result = []
        start = 0
        word_length = 0

        for i in range(len(words)):
            if word_length + len(words[i]) + i - start > maxWidth:
                result.append(justify_line(words, maxWidth, start, i-1))
                start = i
                word_length = len(words[i])
            else:
                word_length += len(words[i])

        result.append(justify_line(words, maxWidth, start, len(words) - 1, is_last=True))

        return result
