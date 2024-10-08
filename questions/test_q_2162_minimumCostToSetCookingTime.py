import pytest
from q_2162_minimumCostToSetCookingTime import Solution


@pytest.mark.parametrize(
    "startAt, moveCost, pushCost, targetSeconds, output",
    [(1, 2, 1, 600, 6), (0, 1, 2, 76, 6)],
)
class TestSolution:
    def test_minCostSetTime(
        self,
        startAt: int,
        moveCost: int,
        pushCost: int,
        targetSeconds: int,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minCostSetTime(
                startAt,
                moveCost,
                pushCost,
                targetSeconds,
            )
            == output
        )
