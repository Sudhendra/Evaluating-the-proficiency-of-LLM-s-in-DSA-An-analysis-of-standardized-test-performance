from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if len(startGene) != len(endGene):
            return -1

        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = [(startGene, 0)]

        while queue:
            gene, mutations = queue.pop(0)

            if gene == endGene:
                return mutations
            
            for i in range(len(gene)):
                for char in 'ACGT':
                    if char != gene[i]:
                        new_gene = gene[:i] + char + gene[i+1:]
                        if new_gene in bank_set:
                            queue.append((new_gene, mutations + 1))
                            bank_set.remove(new_gene)

        return -1