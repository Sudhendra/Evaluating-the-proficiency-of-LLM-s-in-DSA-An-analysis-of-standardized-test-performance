import pytest
from q_2651_calculateDelayedArrivalTime import Solution


@pytest.mark.parametrize("arrivalTime, delayedTime, output", [(15, 5, 20), (13, 11, 0)])
class TestSolution:
    def test_findDelayedArrivalTime(
        self, arrivalTime: int, delayedTime: int, output: int
    ):
        sc = Solution()
        assert (
            sc.findDelayedArrivalTime(
                arrivalTime,
                delayedTime,
            )
            == output
        )
