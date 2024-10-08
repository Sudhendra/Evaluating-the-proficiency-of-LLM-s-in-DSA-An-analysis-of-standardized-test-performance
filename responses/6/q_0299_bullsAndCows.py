class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        cows = sum(min(secret.count(digit), guess.count(digit)) for digit in set(secret)) - bulls
        return f"{bulls}A{cows}B"
