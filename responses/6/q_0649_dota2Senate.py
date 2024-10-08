class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q = []
        dire_q = []

        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                radiant_q.append(i)
            else:
                dire_q.append(i)

        while len(radiant_q) > 0 and len(dire_q) > 0:
            if radiant_q[0] < dire_q[0]:
                radiant_q.append(radiant_q[0] + n)
            else:
                dire_q.append(dire_q[0] + n)

            radiant_q.pop(0)
            dire_q.pop(0)

        return "Radiant" if len(radiant_q) > 0 else "Dire"
