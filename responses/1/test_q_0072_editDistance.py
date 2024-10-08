import pytest
from q_0072_editDistance import Solution


@pytest.mark.parametrize(
    "word1, word2, output", [("horse", "ros", 3), ("intention", "execution", 5)]
)
class TestSolution:
    def test_minDistance(self, word1: str, word2: str, output: int):
        sc = Solution()
        assert (
            sc.minDistance(
                word1,
                word2,
            )
            == output
        )
