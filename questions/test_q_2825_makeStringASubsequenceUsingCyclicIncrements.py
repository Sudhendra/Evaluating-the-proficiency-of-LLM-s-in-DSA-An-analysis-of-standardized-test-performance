import pytest
from q_2825_makeStringASubsequenceUsingCyclicIncrements import Solution


@pytest.mark.parametrize(
    "str1, str2, output", [("abc", "ad", True), ("zc", "ad", True), ("ab", "d", False)]
)
class TestSolution:
    def test_canMakeSubsequence(self, str1: str, str2: str, output: bool):
        sc = Solution()
        assert (
            sc.canMakeSubsequence(
                str1,
                str2,
            )
            == output
        )
