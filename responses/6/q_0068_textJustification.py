from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            line = words[i]
            total_len = len(words[i])
            word_count = 1

            while i + word_count < len(words) and total_len + len(words[i + word_count]) + word_count <= maxWidth:
                total_len += len(words[i + word_count])
                word_count += 1

            if word_count > 1 and i + word_count < len(words):
                spaces = maxWidth - total_len
                space_between_words, extra_spaces = divmod(spaces, word_count - 1)
                line = (" " * (space_between_words + 1)).join(words[i:i + extra_spaces + 1])
                line += " " * space_between_words
                line += (" " * space_between_words).join(words[i + extra_spaces + 1:i + word_count])

            else:
                line += " " * (maxWidth - total_len)

            result.append(line)
            i += word_count

        result[-1] = " ".join(words[i:len(words)]) + " " * (maxWidth - len(" ".join(words[i:len(words)])))

        return result
