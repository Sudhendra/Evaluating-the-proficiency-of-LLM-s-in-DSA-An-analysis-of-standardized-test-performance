from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant.popleft() + len(senate))
                dire.popleft()
            else:
                dire.append(dire.popleft() + len(senate))
                radiant.popleft()

        return "Radiant" if radiant else "Dire"
