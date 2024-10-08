import pytest
from q_1079_letterTilePossibilities import Solution


@pytest.mark.parametrize("tiles, output", [("AAB", 8), ("AAABBC", 188), ("V", 1)])
class TestSolution:
    def test_numTilePossibilities(self, tiles: str, output: int):
        sc = Solution()
        assert (
            sc.numTilePossibilities(
                tiles,
            )
            == output
        )
