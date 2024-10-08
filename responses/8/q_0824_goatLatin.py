class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        words = sentence.split()
        
        result = []
        for i, word in enumerate(words, 1):
            if word[0].lower() in vowels:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            
            word += 'a' * i
            result.append(word)
        
        return ' '.join(result)
