from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        bankSet = set(bank)
        queue = deque([(startGene, 0)])
        visited = set()

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for ch in ['A', 'C', 'G', 'T']:
                    if ch != gene[i]:
                        newGene = gene[:i] + ch + gene[i+1:]
                        if newGene in bankSet and newGene not in visited:
                            queue.append((newGene, steps + 1))
                            visited.add(newGene)

        return -1
