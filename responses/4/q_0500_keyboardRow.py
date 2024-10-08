from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        def check_word(word):
            row_set = None
            for c in word:
                c_lower = c.lower()
                if row_set is None:
                    if c_lower in row1:
                        row_set = row1
                    elif c_lower in row2:
                        row_set = row2
                    elif c_lower in row3:
                        row_set = row3
                elif c_lower not in row_set:
                    return False
            return True

        return [word for word in words if check_word(word)]

# Example usage
sol = Solution()
input_words = ["Hello", "Alaska", "Dad", "Peace"]
output = sol.findWords(input_words)
print(output)
