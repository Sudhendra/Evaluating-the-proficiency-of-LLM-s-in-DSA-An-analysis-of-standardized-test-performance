import pytest
from q_1094_carPooling import Solution


@pytest.mark.parametrize(
    "trips, capacity, output",
    [([[2, 1, 5], [3, 3, 7]], 4, False), ([[2, 1, 5], [3, 3, 7]], 5, True)],
)
class TestSolution:
    def test_carPooling(self, trips: List[List[int]], capacity: int, output: bool):
        sc = Solution()
        assert (
            sc.carPooling(
                trips,
                capacity,
            )
            == output
        )
