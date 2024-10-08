import pytest
from q_2087_minimumCostHomecomingOfARobotInAGrid import Solution


@pytest.mark.parametrize(
    "startPos, homePos, rowCosts, colCosts, output",
    [([1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7], 18), ([0, 0], [0, 0], [5], [26], 0)],
)
class TestSolution:
    def test_minCost(
        self,
        startPos: List[int],
        homePos: List[int],
        rowCosts: List[int],
        colCosts: List[int],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minCost(
                startPos,
                homePos,
                rowCosts,
                colCosts,
            )
            == output
        )
