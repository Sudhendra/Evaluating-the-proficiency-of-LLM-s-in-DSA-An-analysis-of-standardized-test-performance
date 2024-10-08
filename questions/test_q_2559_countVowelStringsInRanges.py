import pytest
from q_2559_countVowelStringsInRanges import Solution


@pytest.mark.parametrize(
    "words, queries, output",
    [
        (["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]], [2, 3, 0]),
        (["a", "e", "i"], [[0, 2], [0, 1], [2, 2]], [3, 2, 1]),
    ],
)
class TestSolution:
    def test_vowelStrings(
        self, words: List[str], queries: List[List[int]], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.vowelStrings(
                words,
                queries,
            )
            == output
        )
