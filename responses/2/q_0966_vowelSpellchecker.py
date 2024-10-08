from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)

        def capitalize(word):
            return word.lower()

        wordlist_set = set(wordlist)
        wordlist_lower = {word.lower(): word for word in wordlist}
        wordlist_devowel = {devowel(word.lower()): word for word in wordlist}

        def correct(query):
            if query in wordlist_set:
                return query
            lowered = query.lower()
            if lowered in wordlist_lower:
                return wordlist_lower[lowered]
            devoweled = devowel(lowered)
            if devoweled in wordlist_devowel:
                return wordlist_devowel[devoweled]
            return ""
        
        return [correct(query) for query in queries]
