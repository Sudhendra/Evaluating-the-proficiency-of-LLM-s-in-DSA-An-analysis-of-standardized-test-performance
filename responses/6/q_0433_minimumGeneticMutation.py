from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        bankSet = set(bank)
        queue = [(startGene, 0)]

        while queue:
            gene, mutations = queue.pop(0)

            if gene == endGene:
                return mutations

            for i in range(len(gene)):
                for c in 'ACGT':
                    newGene = gene[:i] + c + gene[i+1:]
                    if newGene in bankSet:
                        bankSet.remove(newGene)
                        queue.append((newGene, mutations + 1))

        return -1
