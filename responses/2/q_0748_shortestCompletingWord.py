class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def count_chars(s):
            char_count = {}
            for char in s:
                if char.isalpha():
                    char = char.lower()
                    char_count[char] = char_count.get(char, 0) + 1
            return char_count
        
        lp_chars = count_chars(licensePlate)
        result = None
        for word in words:
            word_chars = count_chars(word)
            if all(lp_chars[char] <= word_chars.get(char, 0) for char in lp_chars):
                if result is None or len(word) < len(result):
                    result = word
        
        return result