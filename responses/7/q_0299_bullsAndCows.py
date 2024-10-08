class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        secret_count = {}
        guess_count = {}

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1

        for k in secret_count:
            cows += min(secret_count[k], guess_count.get(k, 0))

        return f"{bulls}A{cows}B"
