from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replace_vowels(word):
            return "".join(['*' if c.lower() in 'aeiou' else c for c in word.lower()])
        
        wordlist_lower = {word.lower(): word for word in wordlist}
        wordlist_vowels = {replace_vowels(word): word for word in wordlist}
        
        def check_query(query):
            if query in wordlist:
                return query
            query_lower = query.lower()
            if query_lower in wordlist_lower:
                return wordlist_lower[query_lower]
            query_vowels = replace_vowels(query)
            if query_vowels in wordlist_vowels:
                return wordlist_vowels[query_vowels]
            return ""
        
        return [check_query(query) for query in queries]
