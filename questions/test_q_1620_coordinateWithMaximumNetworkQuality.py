import pytest
from q_1620_coordinateWithMaximumNetworkQuality import Solution


@pytest.mark.parametrize(
    "towers, radius, output",
    [
        ([[1, 2, 5], [2, 1, 7], [3, 1, 9]], 2, [2, 1]),
        ([[23, 11, 21]], 9, [23, 11]),
        ([[1, 2, 13], [2, 1, 7], [0, 1, 9]], 2, [1, 2]),
    ],
)
class TestSolution:
    def test_bestCoordinate(
        self, towers: List[List[int]], radius: int, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.bestCoordinate(
                towers,
                radius,
            )
            == output
        )
