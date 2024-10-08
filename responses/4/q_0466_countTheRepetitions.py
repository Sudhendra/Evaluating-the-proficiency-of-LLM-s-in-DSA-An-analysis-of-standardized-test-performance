def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
    if not set(s2).issubset(set(s1)):
        return 0

    counts = [0] * (len(s2) + 1)
    remains = [0] * (len(s2) + 1)
    j, count = 0, 0

    for k in range(1, n1 + 1):
        for i in range(len(s1)):
            if s1[i] == s2[j]:
                j += 1
                if j == len(s2):
                    j = 0
                    count += 1

        counts[k] = count
        remains[k] = j

        if j in remains[:k]:
            start = remains.index(j)
            prefix_counts = counts[start]
            pattern_counts = (n1 - start) // (k - start) * (counts[k] - counts[start])
            suffix_counts = counts[start + (n1 - start) % (k - start)] - counts[start]
            return (prefix_counts + pattern_counts + suffix_counts) // n2

    return counts[n1] // n2
