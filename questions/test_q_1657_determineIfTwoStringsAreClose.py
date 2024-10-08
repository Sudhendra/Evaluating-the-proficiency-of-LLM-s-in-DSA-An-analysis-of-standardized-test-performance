import pytest
from q_1657_determineIfTwoStringsAreClose import Solution


@pytest.mark.parametrize(
    "word1, word2, output",
    [("abc", "bca", True), ("a", "aa", False), ("cabbba", "abbccc", True)],
)
class TestSolution:
    def test_closeStrings(self, word1: str, word2: str, output: bool):
        sc = Solution()
        assert (
            sc.closeStrings(
                word1,
                word2,
            )
            == output
        )
