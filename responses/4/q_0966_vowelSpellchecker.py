from typing import List, Dict

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_set = set(wordlist)
        word_cap = {}
        word_vowel = {}

        def devowel(word: str) -> str:
            return ''.join('*' if c in 'aeiou' else c.lower() for c in word)

        for word in wordlist:
            word_cap.setdefault(word.lower(), word)
            word_vowel.setdefault(devowel(word), word)

        def check_word(query: str) -> str:
            if query in word_set:
                return query
            lowercase = query.lower()
            if lowercase in word_cap:
                return word_cap[lowercase]
            devoweled = devowel(query)
            if devoweled in word_vowel:
                return word_vowel[devoweled]
            return ''

        return [check_word(query) for query in queries]
