import pytest
from q_1893_checkIfAllTheIntegersInARangeAreCovered import Solution


@pytest.mark.parametrize(
    "ranges, left, right, output",
    [([[1, 2], [3, 4], [5, 6]], 2, 5, True), ([[1, 10], [10, 20]], 21, 21, False)],
)
class TestSolution:
    def test_isCovered(
        self, ranges: List[List[int]], left: int, right: int, output: bool
    ):
        sc = Solution()
        assert (
            sc.isCovered(
                ranges,
                left,
                right,
            )
            == output
        )
