class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        result = []
        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                new_word = word + 'ma' + 'a' * i
            else:
                new_word = word[1:] + word[0] + 'ma' + 'a' * i
            result.append(new_word)
        return ' '.join(result)