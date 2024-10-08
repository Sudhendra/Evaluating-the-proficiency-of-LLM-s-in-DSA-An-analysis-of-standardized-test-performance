from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replace_vowels(word: str) -> str:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return ''.join(v if v.lower() not in vowels else '*' for v in word)

        def spell_checker_helper(query: str) -> str:
            if query in wordlist:
                return query

            query_lower = query.lower()
            for word in wordlist:
                if word.lower() == query_lower:
                    return word

            query_vowels = replace_vowels(query_lower)
            for word in wordlist:
                if replace_vowels(word.lower()) == query_vowels:
                    return word
            
            return ""

        return [spell_checker_helper(query) for query in queries]
