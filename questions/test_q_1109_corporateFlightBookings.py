import pytest
from q_1109_corporateFlightBookings import Solution


@pytest.mark.parametrize(
    "bookings, n, output",
    [
        ([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5, [10, 55, 45, 25, 25]),
        ([[1, 2, 10], [2, 2, 15]], 2, [10, 25]),
    ],
)
class TestSolution:
    def test_corpFlightBookings(
        self, bookings: List[List[int]], n: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.corpFlightBookings(
                bookings,
                n,
            )
            == output
        )
