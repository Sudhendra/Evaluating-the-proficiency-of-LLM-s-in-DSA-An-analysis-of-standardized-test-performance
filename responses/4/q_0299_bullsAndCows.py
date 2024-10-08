from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        
        secret_count = Counter(secret)
        guess_count = Counter(guess)
        
        cows = sum(min(secret_count[c], guess_count[c]) for c in secret_count if c in guess_count) - bulls
        
        return f"{bulls}A{cows}B"
