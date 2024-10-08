from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            line_words = []
            line_length = 0

            # Calculate how many words can fit in a line
            while i < len(words) and line_length + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1

            spaces_to_add = maxWidth - line_length
            num_words = len(line_words)

            # If there is more than one word and it's not the last line
            if num_words > 1 and i < len(words):
                space_between_words = spaces_to_add // (num_words - 1)
                extra_spaces = spaces_to_add % (num_words - 1)
                new_line = ""

                for j in range(num_words):
                    new_line += line_words[j]
                    if j < num_words - 1:
                        new_line += " " * space_between_words
                        if extra_spaces > 0:
                            new_line += " "
                            extra_spaces -= 1
            else:
                new_line = " ".join(line_words)
                new_line += " " * (maxWidth - len(new_line))

            result.append(new_line)

        return result
