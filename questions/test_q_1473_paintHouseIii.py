import pytest
from q_1473_paintHouseIii import Solution


@pytest.mark.parametrize(
    "houses, cost, m, n, target, output",
    [
        ([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 9),
        ([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 11),
        ([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3, -1),
    ],
)
class TestSolution:
    def test_minCost(
        self,
        houses: List[int],
        cost: List[List[int]],
        m: int,
        n: int,
        target: int,
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minCost(
                houses,
                cost,
                m,
                n,
                target,
            )
            == output
        )
