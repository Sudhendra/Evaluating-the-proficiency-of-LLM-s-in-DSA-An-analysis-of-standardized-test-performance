class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        def convert_word(word, index):
            if word[0].lower() in vowels:
                return word + 'ma' + 'a' * (index + 1)
            else:
                return word[1:] + word[0] + 'ma' + 'a' * (index + 1)
        
        words = sentence.split()
        
        return ' '.join(convert_word(word, index) for index, word in enumerate(words))
