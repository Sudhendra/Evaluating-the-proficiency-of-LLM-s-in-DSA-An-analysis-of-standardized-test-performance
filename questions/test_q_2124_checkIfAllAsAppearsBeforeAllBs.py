import pytest
from q_2124_checkIfAllAsAppearsBeforeAllBs import Solution


@pytest.mark.parametrize(
    "s, output", [("aaabbb", True), ("abab", False), ("bbb", True)]
)
class TestSolution:
    def test_checkString(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.checkString(
                s,
            )
            == output
        )
