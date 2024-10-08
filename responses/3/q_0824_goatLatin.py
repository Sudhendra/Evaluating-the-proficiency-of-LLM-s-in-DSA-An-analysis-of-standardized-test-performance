class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def goat_latin_word(word, index):
            vowels = set("aeiouAEIOU")

            if word[0] in vowels:
                return word + "ma" + "a" * (index + 1)
            else:
                return word[1:] + word[0] + "ma" + "a" * (index + 1)

        words = sentence.split()
        goat_latin_words = [goat_latin_word(word, index) for index, word in enumerate(words)]

        return " ".join(goat_latin_words)