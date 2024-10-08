import pytest
from q_1801_numberOfOrdersInTheBacklog import Solution


@pytest.mark.parametrize(
    "orders, output",
    [
        ([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]], 6),
        ([[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]], 999999984),
    ],
)
class TestSolution:
    def test_getNumberOfBacklogOrders(self, orders: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.getNumberOfBacklogOrders(
                orders,
            )
            == output
        )
