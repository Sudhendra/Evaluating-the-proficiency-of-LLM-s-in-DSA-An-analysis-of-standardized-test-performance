import pytest
from q_1184_distanceBetweenBusStops import Solution


@pytest.mark.parametrize(
    "distance, start, destination, output",
    [([1, 2, 3, 4], 0, 1, 1), ([1, 2, 3, 4], 0, 2, 3), ([1, 2, 3, 4], 0, 3, 4)],
)
class TestSolution:
    def test_distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int, output: int
    ):
        sc = Solution()
        assert (
            sc.distanceBetweenBusStops(
                distance,
                start,
                destination,
            )
            == output
        )
