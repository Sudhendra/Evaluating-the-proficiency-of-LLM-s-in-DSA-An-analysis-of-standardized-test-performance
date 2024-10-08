class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)
        for t in trust:
            trust_count[t[0]] -= 1  # decrement trust count for person trusting
            trust_count[t[1]] += 1  # increment trust count for person being trusted

        for i in range(1, n + 1):
            if trust_count[i] == n - 1:  # Check if a person is trusted by all others
                return i

        return -1