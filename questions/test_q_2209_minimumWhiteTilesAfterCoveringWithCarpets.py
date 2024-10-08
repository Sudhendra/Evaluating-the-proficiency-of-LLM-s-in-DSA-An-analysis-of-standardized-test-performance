import pytest
from q_2209_minimumWhiteTilesAfterCoveringWithCarpets import Solution


@pytest.mark.parametrize(
    "floor, numCarpets, carpetLen, output", [("10110101", 2, 2, 2), ("11111", 2, 3, 0)]
)
class TestSolution:
    def test_minimumWhiteTiles(
        self, floor: str, numCarpets: int, carpetLen: int, output: int
    ):
        sc = Solution()
        assert (
            sc.minimumWhiteTiles(
                floor,
                numCarpets,
                carpetLen,
            )
            == output
        )
