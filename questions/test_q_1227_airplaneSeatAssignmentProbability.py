import pytest
from q_1227_airplaneSeatAssignmentProbability import Solution


@pytest.mark.parametrize("n, output", [(1, 1.0), (2, 0.5)])
class TestSolution:
    def test_nthPersonGetsNthSeat(self, n: int, output: float):
        sc = Solution()
        assert (
            sc.nthPersonGetsNthSeat(
                n,
            )
            == output
        )
