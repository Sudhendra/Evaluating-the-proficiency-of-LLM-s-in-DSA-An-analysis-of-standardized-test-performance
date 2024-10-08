class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue, dire_queue = [], []
        n = len(senate)
        
        for i, party in enumerate(senate):
            if party == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)
        
        while radiant_queue and dire_queue:
            radiant_index = radiant_queue.pop(0)
            dire_index = dire_queue.pop(0)
            
            if radiant_index < dire_index:
                radiant_queue.append(radiant_index + n)
            else:
                dire_queue.append(dire_index + n)
        
        return "Radiant" if radiant_queue else "Dire"