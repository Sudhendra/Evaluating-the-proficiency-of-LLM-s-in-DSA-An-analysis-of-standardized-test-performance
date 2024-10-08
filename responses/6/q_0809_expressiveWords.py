class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word: str) -> bool:
            i, j, count_i, count_j = 0, 0, 0, 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False

                while i < len(s) and s[i] == word[j]:
                    count_i += 1
                    i += 1

                while j < len(word) and word[j] == word[j]:
                    count_j += 1
                    j += 1

                if count_i < 3:
                    if count_i != count_j:
                        return False
                elif count_i < count_j:
                    return False

                count_i = 0
                count_j = 0

            return i == len(s) and j == len(word)

        count = 0
        for word in words:
            if is_stretchy(word):
                count += 1

        return count
