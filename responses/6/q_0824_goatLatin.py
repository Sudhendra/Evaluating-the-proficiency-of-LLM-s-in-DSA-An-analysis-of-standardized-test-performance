class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')

        def goatify(word, idx):
            if word[0] in vowels:
                return word + 'ma' + 'a' * (idx + 1)
            else:
                return word[1:] + word[0] + 'ma' + 'a' * (idx + 1)

        new_sentence = []
        for idx, word in enumerate(sentence.split()):
            new_sentence.append(goatify(word, idx))

        return ' '.join(new_sentence)
