class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []
        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                result.append(word + "ma" + "a"*i)
            else:
                result.append(word[1:] + word[0] + "ma" + "a"*i)
        return " ".join(result)