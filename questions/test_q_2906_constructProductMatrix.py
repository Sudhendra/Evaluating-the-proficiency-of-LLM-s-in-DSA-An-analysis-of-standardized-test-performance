import pytest
from q_2906_constructProductMatrix import Solution


@pytest.mark.parametrize(
    "grid, output",
    [([[1, 2], [3, 4]], [[24, 12], [8, 6]]), ([[12345], [2], [1]], [[2], [0], [0]])],
)
class TestSolution:
    def test_constructProductMatrix(
        self, grid: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.constructProductMatrix(
                grid,
            )
            == output
        )
