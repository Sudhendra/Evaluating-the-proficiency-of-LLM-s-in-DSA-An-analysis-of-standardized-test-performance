from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replace_vowels(word):
            vowels = set('aeiou')
            return ''.join('*' if char.lower() in vowels else char for char in word)
        
        word_set = set(wordlist)
        word_dict = {}
        vowel_dict = {}
        
        for word in wordlist:
            word_lower = word.lower()
            word_dict.setdefault(word_lower, word)
            vowel_key = ''.join('*' if char.lower() in set('aeiou') else char for char in word_lower)
            vowel_dict.setdefault(vowel_key, word)
        
        result = []
        for query in queries:
            if query in word_set:
                result.append(query)
                continue
            query_lower = query.lower()
            if query_lower in word_dict:
                result.append(word_dict[query_lower])
                continue
            vowel_key = ''.join('*' if char.lower() in set('aeiou') else char for char in query_lower)
            if vowel_key in vowel_dict:
                result.append(vowel_dict[vowel_key])
                continue
            result.append("")
        
        return result
