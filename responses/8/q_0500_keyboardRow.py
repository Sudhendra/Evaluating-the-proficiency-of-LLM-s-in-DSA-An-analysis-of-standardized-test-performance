class Solution:
    def findWords(self, words):
        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        
        for word in words:
            lowercase_word = word.lower()
            in_row = False
            for row in keyboard_rows:
                if all(letter in row for letter in lowercase_word):
                    in_row = True
                    break
            if in_row:
                result.append(word)
        
        return result
