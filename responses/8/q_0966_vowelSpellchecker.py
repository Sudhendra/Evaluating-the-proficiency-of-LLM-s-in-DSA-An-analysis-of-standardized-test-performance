from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def vowel_error(word):
            vowels = ('a', 'e', 'i', 'o', 'u')
            variations = set()
            for c in vowels:
                variations.add(word.replace(c, '_'))
            return variations

        def correct_word(wordlist, query):
            if query in wordlist:
                return query

            lower_query = query.lower()
            if lower_query in map(str.lower, wordlist):
                return wordlist[[w.lower() for w in wordlist].index(lower_query)]

            vowel_errors = vowel_error(query.lower())
            for i, word in enumerate(wordlist):
                if word.lower() in vowel_errors:
                    return word

            return ""

        return [correct_word(wordlist, query) for query in queries]
