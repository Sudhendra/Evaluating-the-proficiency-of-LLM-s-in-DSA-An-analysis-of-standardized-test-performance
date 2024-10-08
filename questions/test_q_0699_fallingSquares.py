import pytest
from q_0699_fallingSquares import Solution


@pytest.mark.parametrize(
    "positions, output",
    [([[1, 2], [2, 3], [6, 1]], [2, 5, 5]), ([[100, 100], [200, 100]], [100, 100])],
)
class TestSolution:
    def test_fallingSquares(self, positions: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.fallingSquares(
                positions,
            )
            == output
        )
