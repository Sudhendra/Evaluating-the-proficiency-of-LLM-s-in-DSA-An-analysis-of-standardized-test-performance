import pytest
from q_0392_isSubsequence import Solution


@pytest.mark.parametrize(
    "s, t, output", [("abc", "ahbgdc", True), ("axc", "ahbgdc", False)]
)
class TestSolution:
    def test_isSubsequence(self, s: str, t: str, output: bool):
        sc = Solution()
        assert (
            sc.isSubsequence(
                s,
                t,
            )
            == output
        )
