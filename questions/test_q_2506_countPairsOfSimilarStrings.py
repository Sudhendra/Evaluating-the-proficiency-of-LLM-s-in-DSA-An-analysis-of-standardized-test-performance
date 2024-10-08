import pytest
from q_2506_countPairsOfSimilarStrings import Solution


@pytest.mark.parametrize(
    "words, output",
    [
        (["aba", "aabb", "abcd", "bac", "aabc"], 2),
        (["aabb", "ab", "ba"], 3),
        (["nba", "cba", "dba"], 0),
    ],
)
class TestSolution:
    def test_similarPairs(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.similarPairs(
                words,
            )
            == output
        )
