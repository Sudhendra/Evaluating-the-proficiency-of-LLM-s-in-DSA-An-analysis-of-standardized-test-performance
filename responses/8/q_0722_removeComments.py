from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_comment_block = False
        result = []
        new_line = ""
        
        for line in source:
            i = 0
            while i < len(line):
                if in_comment_block:
                    if line[i:i+2] == "*/":
                        in_comment_block = False
                        i += 2
                else:
                    if line[i:i+2] == "//":
                        break
                    elif line[i:i+2] == "/*":
                        in_comment_block = True
                        i += 1
                    else:
                        new_line += line[i]
                i += 1
            
            if not in_comment_block and new_line:
                result.append(new_line)
                new_line = ""
        
        return result
