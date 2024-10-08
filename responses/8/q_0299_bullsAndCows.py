class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        both_count = sum(min(secret.count(x), guess.count(x)) for x in set(secret))
        return f"{bulls}A{both_count - bulls}B"
