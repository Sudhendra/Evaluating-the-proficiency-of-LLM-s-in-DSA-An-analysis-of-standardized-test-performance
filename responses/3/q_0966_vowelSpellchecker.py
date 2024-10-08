class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def remove_vowels(word):
            return ''.join('*' if char in 'aeiou' else char for char in word.lower())

        wordlist_lower = {word.lower(): word for word in wordlist}
        wordlist_vowel = {remove_vowels(word): word for word in wordlist}

        def spell_check(query):
            if query in wordlist:
                return query
            query_lower = query.lower()

            if query_lower in wordlist_lower:
                return wordlist_lower[query_lower]
            
            query_vowel = remove_vowels(query)
            if query_vowel in wordlist_vowel:
                return wordlist_vowel[query_vowel]

            return ""

        return [spell_check(query) for query in queries]