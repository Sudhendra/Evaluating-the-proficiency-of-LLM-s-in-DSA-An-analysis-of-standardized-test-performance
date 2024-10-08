class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_order = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                
                if words[i][j] != words[i + 1][j]:
                    if alien_order[words[i][j]] > alien_order[words[i + 1][j]]:
                        return False
                    break

        return True
