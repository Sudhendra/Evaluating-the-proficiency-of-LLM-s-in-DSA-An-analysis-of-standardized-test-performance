class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        i = 0
        n = len(formula)

        def parse_counts():
            nonlocal i, n
            counts = {}
            if i < n and formula[i] == "(":
                i += 1
                while i < n and formula[i] != ")":
                    atom, count = parse_atom_count()
                    counts[atom] = counts.get(atom, 0) + count
                i += 1
                count = parse_count()
                for atom in counts:
                    counts[atom] *= count
            return counts

        def parse_atom_count():
            nonlocal i, n
            atom = formula[i]
            i += 1
            while i < n and formula[i].islower():
                atom += formula[i]
                i += 1
            count = parse_count()
            return atom, count

        def parse_count():
            nonlocal i, n
            count = 0
            while i < n and formula[i].isdigit():
                count = count * 10 + int(formula[i])
                i += 1
            return count if count > 0 else 1

        counts = parse_counts()

        result = ""
        for atom in sorted(counts):
            result += atom
            if counts[atom] > 1:
                result += str(counts[atom])

        return result
