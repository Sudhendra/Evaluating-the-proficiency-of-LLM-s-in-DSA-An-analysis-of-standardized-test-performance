from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        mutations = {'A', 'C', 'G', 'T'}
        queue = deque([(startGene, 0)])

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for m in mutations:
                    new_gene = gene[:i] + m + gene[i+1:]
                    if new_gene in bank_set:
                        queue.append((new_gene, steps + 1))
                        bank_set.remove(new_gene)

        return -1
