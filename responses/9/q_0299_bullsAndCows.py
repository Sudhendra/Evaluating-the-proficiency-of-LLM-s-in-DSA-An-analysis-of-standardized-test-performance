class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        secret_counts = [0] * 10
        guess_counts = [0] * 10
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counts[int(s)] += 1
                guess_counts[int(g)] += 1
        
        for i in range(10):
            cows += min(secret_counts[i], guess_counts[i])
        
        return str(bulls) + 'A' + str(cows) + 'B'
