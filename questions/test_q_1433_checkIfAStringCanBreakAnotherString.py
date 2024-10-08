import pytest
from q_1433_checkIfAStringCanBreakAnotherString import Solution


@pytest.mark.parametrize(
    "s1, s2, output",
    [("abc", "xya", True), ("abe", "acd", False), ("leetcodee", "interview", True)],
)
class TestSolution:
    def test_checkIfCanBreak(self, s1: str, s2: str, output: bool):
        sc = Solution()
        assert (
            sc.checkIfCanBreak(
                s1,
                s2,
            )
            == output
        )
