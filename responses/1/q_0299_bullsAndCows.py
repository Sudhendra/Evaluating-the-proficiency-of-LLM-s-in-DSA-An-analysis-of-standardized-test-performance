class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        secret_count = {}
        guess_count = {}
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
                guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1
        
        for num in secret_count:
            if num in guess_count:
                cows += min(secret_count[num], guess_count[num])
        
        return f"{bulls}A{cows}B"
