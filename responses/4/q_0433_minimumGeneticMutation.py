from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        bank = set(bank)
        mutations = {'A', 'C', 'G', 'T'}
        
        queue = deque([(startGene, 0)])
        
        while queue:
            gene, mutations_count = queue.popleft()
            
            if gene == endGene:
                return mutations_count
            
            for i in range(len(gene)):
                for mutation in mutations:
                    mutated_gene = gene[:i] + mutation + gene[i + 1:]
                    if mutated_gene in bank:
                        bank.remove(mutated_gene)
                        queue.append((mutated_gene, mutations_count + 1))
        
        return -1
