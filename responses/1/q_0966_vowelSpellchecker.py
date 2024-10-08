from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replace_vowels_with_placeholder(word):
            return ''.join(['#' if char.lower() in 'aeiou' else char.lower() for char in word])

        words_set = set(wordlist)
        words_lower_map = {word.lower(): word for word in wordlist}
        words_vowel_map = {replace_vowels_with_placeholder(word.lower()): word for word in wordlist}

        def check_word(word):
            if word in words_set:
                return word
            lower_case = word.lower()
            if lower_case in words_lower_map:
                return words_lower_map[lower_case]
            replaced_vowels = replace_vowels_with_placeholder(lower_case)
            if replaced_vowels in words_vowel_map:
                return words_vowel_map[replaced_vowels]
            return ""

        return [check_word(query) for query in queries]