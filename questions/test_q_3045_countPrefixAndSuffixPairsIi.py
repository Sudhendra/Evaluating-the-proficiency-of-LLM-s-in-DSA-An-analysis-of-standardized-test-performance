import pytest
from q_3045_countPrefixAndSuffixPairsIi import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["a", "aba", "ababa", "aa"], 4),
        (["pa", "papa", "ma", "mama"], 2),
        (["abab", "ab"], 0),
    ],
)
class TestSolution:
    def test_countPrefixSuffixPairs(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.countPrefixSuffixPairs(
                words,
            )
            == output
        )
