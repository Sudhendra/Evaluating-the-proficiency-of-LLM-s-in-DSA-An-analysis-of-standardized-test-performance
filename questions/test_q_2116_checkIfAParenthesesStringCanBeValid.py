import pytest
from q_2116_checkIfAParenthesesStringCanBeValid import Solution


@pytest.mark.parametrize(
    "s, locked, output",
    [("))()))", "010100", True), ("()()", "0000", True), (")", "0", False)],
)
class TestSolution:
    def test_canBeValid(self, s: str, locked: str, output: bool):
        sc = Solution()
        assert (
            sc.canBeValid(
                s,
                locked,
            )
            == output
        )
