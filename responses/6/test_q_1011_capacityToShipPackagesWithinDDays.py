from typing import List
import pytest
from q_1011_capacityToShipPackagesWithinDDays import Solution


@pytest.mark.parametrize(
    "weights, days, output",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
    ],
)
class TestSolution:
    def test_shipWithinDays(self, weights: List[int], days: int, output: int):
        sc = Solution()
        assert (
            sc.shipWithinDays(
                weights,
                days,
            )
            == output
        )
