from collections import deque

class Solution:

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        queue = deque([(startGene, 0)])
        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            
            for i in range(len(gene)):
                for nucleotide in "ACGT":
                    new_gene = gene[:i] + nucleotide + gene[i+1:]
                    if new_gene in bank:
                        bank.remove(new_gene)
                        queue.append((new_gene, mutations + 1))
        
        return -1
