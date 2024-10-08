class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        bank_set = set(bank)
        queue = collections.deque([(startGene, 0)])

        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            
            for i in range(len(gene)):
                for char in 'ACGT':
                    new_gene = gene[:i] + char + gene[i+1:]
                    if new_gene in bank_set:
                        bank_set.remove(new_gene)
                        queue.append((new_gene, mutations + 1))
        
        return -1