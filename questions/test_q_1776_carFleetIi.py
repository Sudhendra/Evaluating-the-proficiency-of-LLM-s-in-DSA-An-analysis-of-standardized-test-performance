import pytest
from q_1776_carFleetIi import Solution


@pytest.mark.parametrize(
    "cars, output",
    [
        ([[1, 2], [2, 1], [4, 3], [7, 2]], [1.0, -1.0, 3.0, -1.0]),
        ([[3, 4], [5, 4], [6, 3], [9, 1]], [2.0, 1.0, 1.5, -1.0]),
    ],
)
class TestSolution:
    def test_getCollisionTimes(self, cars: List[List[int]], output: List[float]):
        sc = Solution()
        assert (
            sc.getCollisionTimes(
                cars,
            )
            == output
        )
