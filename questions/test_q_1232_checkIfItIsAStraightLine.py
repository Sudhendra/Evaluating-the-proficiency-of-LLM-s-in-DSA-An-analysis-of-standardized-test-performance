import pytest
from q_1232_checkIfItIsAStraightLine import Solution


@pytest.mark.parametrize(
    "coordinates, output",
    [
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
        ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
    ],
)
class TestSolution:
    def test_checkStraightLine(self, coordinates: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.checkStraightLine(
                coordinates,
            )
            == output
        )
