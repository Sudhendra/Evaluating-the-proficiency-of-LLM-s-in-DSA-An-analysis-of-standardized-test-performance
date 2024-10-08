import pytest
from q_2398_maximumNumberOfRobotsWithinBudget import Solution


@pytest.mark.parametrize(
    "chargeTimes, runningCosts, budget, output",
    [([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25, 3), ([11, 12, 19], [10, 8, 7], 19, 0)],
)
class TestSolution:
    def test_maximumRobots(
        self, chargeTimes: List[int], runningCosts: List[int], budget: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maximumRobots(
                chargeTimes,
                runningCosts,
                budget,
            )
            == output
        )
