import pytest
from q_0539_minimumTimeDifference import Solution


@pytest.mark.parametrize(
    "timePoints, output", [(["23:59", "00:00"], 1), (["00:00", "23:59", "00:00"], 0)]
)
class TestSolution:
    def test_findMinDifference(self, timePoints: List[str], output: int):
        sc = Solution()
        assert (
            sc.findMinDifference(
                timePoints,
            )
            == output
        )
