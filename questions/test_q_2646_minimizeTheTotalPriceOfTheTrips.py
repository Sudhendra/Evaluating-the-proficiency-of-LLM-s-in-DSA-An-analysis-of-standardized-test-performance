import pytest
from q_2646_minimizeTheTotalPriceOfTheTrips import Solution


@pytest.mark.parametrize(
    "n, edges, price, trips, output",
    [
        (4, [[0, 1], [1, 2], [1, 3]], [2, 2, 10, 6], [[0, 3], [2, 1], [2, 3]], 23),
        (2, [[0, 1]], [2, 2], [[0, 0]], 1),
    ],
)
class TestSolution:
    def test_minimumTotalPrice(
        self,
        n: int,
        edges: List[List[int]],
        price: List[int],
        trips: List[List[int]],
        output: int,
    ):
        sc = Solution()
        assert (
            sc.minimumTotalPrice(
                n,
                edges,
                price,
                trips,
            )
            == output
        )
