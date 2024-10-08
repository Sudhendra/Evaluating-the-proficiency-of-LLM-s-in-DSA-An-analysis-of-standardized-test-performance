import pytest
from q_0583_deleteOperationForTwoStrings import Solution


@pytest.mark.parametrize(
    "word1, word2, output", [("sea", "eat", 2), ("leetcode", "etco", 4)]
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
