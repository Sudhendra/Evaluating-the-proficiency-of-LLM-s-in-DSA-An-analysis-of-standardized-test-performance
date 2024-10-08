import pytest
from q_0174_dungeonGame import Solution


@pytest.mark.parametrize(
    "dungeon, output", [([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7), ([[0]], 1)]
)
class TestSolution:
    def test_calculateMinimumHP(self, dungeon: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.calculateMinimumHP(
                dungeon,
            )
            == output
        )
