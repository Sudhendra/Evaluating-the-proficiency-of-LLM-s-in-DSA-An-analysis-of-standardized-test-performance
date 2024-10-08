import pytest
from q_2531_makeNumberOfDistinctCharactersEqual import Solution


@pytest.mark.parametrize(
    "word1, word2, output",
    [("ac", "b", False), ("abcc", "aab", True), ("abcde", "fghij", True)],
)
class TestSolution:
    def test_isItPossible(self, word1: str, word2: str, output: bool):
        sc = Solution()
        assert (
            sc.isItPossible(
                word1,
                word2,
            )
            == output
        )
