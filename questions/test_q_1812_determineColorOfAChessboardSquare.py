import pytest
from q_1812_determineColorOfAChessboardSquare import Solution


@pytest.mark.parametrize(
    "coordinates, output", [("a1", False), ("h3", True), ("c7", False)]
)
class TestSolution:
    def test_squareIsWhite(self, coordinates: str, output: bool):
        sc = Solution()
        assert (
            sc.squareIsWhite(
                coordinates,
            )
            == output
        )
