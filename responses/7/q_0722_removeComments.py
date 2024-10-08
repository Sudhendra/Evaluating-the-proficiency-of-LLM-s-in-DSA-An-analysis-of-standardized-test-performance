from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block_comment = False
        output = []
        new_line = ""

        for line in source:
            i = 0
            while i < len(line):
                if not in_block_comment:
                    if line[i:i+2] == "//":
                        break  # ignore the rest of the line
                    elif line[i:i+2] == "/*":
                        in_block_comment = True
                        i += 1
                    else:
                        new_line += line[i]
                else:
                    if line[i:i+2] == "*/":
                        in_block_comment = False
                        i += 1

                i += 1

            if not in_block_comment and new_line:
                output.append(new_line)
                new_line = ""

        return output
