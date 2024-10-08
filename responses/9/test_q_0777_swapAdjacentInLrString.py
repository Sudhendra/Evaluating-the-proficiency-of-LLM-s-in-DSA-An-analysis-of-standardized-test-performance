import pytest
from q_0777_swapAdjacentInLrString import Solution


@pytest.mark.parametrize(
    "start, end, output", [("RXXLRXRXL", "XRLXXRRLX", True), ("X", "L", False)]
)
class TestSolution:
    def test_canTransform(self, start: str, end: str, output: bool):
        sc = Solution()
        assert (
            sc.canTransform(
                start,
                end,
            )
            == output
        )
