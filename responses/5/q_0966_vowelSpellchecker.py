from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def to_vowel_pattern(word):
            vowels = set('aeiou')
            return ''.join('#' if char.lower() in vowels else char.lower() for char in word)

        exact_matches = set(wordlist)
        capitalization_matches = {}
        vowel_pattern_matches = {}
        vowels = set('aeiou')

        for word in wordlist:
            word_lower = word.lower()
            capitalization_matches.setdefault(word_lower, word)
            vowel_pattern = to_vowel_pattern(word_lower)
            vowel_pattern_matches.setdefault(vowel_pattern, word)

        def check(word):
            if word in exact_matches:
                return word
            word_lower = word.lower()
            if word_lower in capitalization_matches:
                return capitalization_matches[word_lower]
            vowel_pattern = to_vowel_pattern(word_lower)
            if vowel_pattern in vowel_pattern_matches:
                return vowel_pattern_matches[vowel_pattern]
            return ""

        return [check(query) for query in queries]
