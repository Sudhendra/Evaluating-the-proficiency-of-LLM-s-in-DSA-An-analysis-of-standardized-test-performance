class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        cows = sum(min(secret.count(char), guess.count(char)) for char in set(secret))
        cows -= bulls
        return f"{bulls}A{cows}B"
