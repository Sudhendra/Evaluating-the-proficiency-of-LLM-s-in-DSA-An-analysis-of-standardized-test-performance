import pytest
from q_1235_maximumProfitInJobScheduling import Solution


@pytest.mark.parametrize(
    "startTime, endTime, profit, output",
    [
        ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
        ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
        ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6),
    ],
)
class TestSolution:
    def test_jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int], output: int
    ):
        sc = Solution()
        assert (
            sc.jobScheduling(
                startTime,
                endTime,
                profit,
            )
            == output
        )
