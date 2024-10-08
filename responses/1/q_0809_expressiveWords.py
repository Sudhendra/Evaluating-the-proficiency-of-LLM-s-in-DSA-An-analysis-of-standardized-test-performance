from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def count_chars(s):
            chars = []
            counts = []
            current_char = ""
            current_count = 0
            for char in s:
                if char != current_char:
                    if current_char:
                        chars.append(current_char)
                        counts.append(current_count)
                    current_char = char
                    current_count = 1
                else:
                    current_count += 1
            chars.append(current_char)
            counts.append(current_count)
            return chars, counts
        
        def compare_chars(s_chars, s_counts, word_chars, word_counts):
            if s_chars != word_chars:
                return False
            for i in range(len(s_chars)):
                if s_counts[i] < 3 and s_counts[i] != word_counts[i]:
                    return False
                if s_counts[i] < word_counts[i]:
                    return False
            return True
        
        s_chars, s_counts = count_chars(s)
        result = 0
        for word in words:
            word_chars, word_counts = count_chars(word)
            if compare_chars(s_chars, s_counts, word_chars, word_counts):
                result += 1
        return result
