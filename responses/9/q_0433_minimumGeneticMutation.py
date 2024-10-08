from typing import List

class Solution:
    
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        queue = [(startGene, 0)]
        
        while queue:
            current_gene, mutations = queue.pop(0)
            
            if current_gene == endGene:
                return mutations
            
            for gene in bank:
                diff_count = sum(c1 != c2 for c1, c2 in zip(current_gene, gene))
                
                if diff_count == 1:
                    queue.append((gene, mutations + 1))
                    bank.remove(gene)
        
        return -1
