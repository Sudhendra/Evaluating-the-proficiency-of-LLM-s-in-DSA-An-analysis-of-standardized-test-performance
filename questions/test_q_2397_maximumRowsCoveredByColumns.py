import pytest
from q_2397_maximumRowsCoveredByColumns import Solution


@pytest.mark.parametrize(
    "matrix, numSelect, output",
    [([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2, 3), ([[1], [0]], 1, 2)],
)
class TestSolution:
    def test_maximumRows(self, matrix: List[List[int]], numSelect: int, output: int):
        sc = Solution()
        assert (
            sc.maximumRows(
                matrix,
                numSelect,
            )
            == output
        )
