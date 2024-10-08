import pytest
from q_2271_maximumWhiteTilesCoveredByACarpet import Solution


@pytest.mark.parametrize(
    "tiles, carpetLen, output",
    [
        ([[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], 10, 9),
        ([[10, 11], [1, 1]], 2, 2),
    ],
)
class TestSolution:
    def test_maximumWhiteTiles(
        self, tiles: List[List[int]], carpetLen: int, output: int
    ):
        sc = Solution()
        assert (
            sc.maximumWhiteTiles(
                tiles,
                carpetLen,
            )
            == output
        )
