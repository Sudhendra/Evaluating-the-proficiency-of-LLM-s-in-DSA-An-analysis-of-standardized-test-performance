import pytest
from q_1849_splittingAStringIntoDescendingConsecutiveValues import Solution


@pytest.mark.parametrize(
    "s, output", [("1234", False), ("050043", True), ("9080701", False)]
)
class TestSolution:
    def test_splitString(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.splitString(
                s,
            )
            == output
        )
