import pytest
from q_1359_countAllValidPickupAndDeliveryOptions import Solution


@pytest.mark.parametrize("n, output", [(1, 1), (2, 6), (3, 90)])
class TestSolution:
    def test_countOrders(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countOrders(
                n,
            )
            == output
        )
