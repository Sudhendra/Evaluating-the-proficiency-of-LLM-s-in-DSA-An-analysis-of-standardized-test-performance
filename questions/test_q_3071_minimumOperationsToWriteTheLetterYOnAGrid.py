import pytest
from q_3071_minimumOperationsToWriteTheLetterYOnAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[1, 2, 2], [1, 1, 0], [0, 1, 0]], 3),
        (
            [
                [0, 1, 0, 1, 0],
                [2, 1, 0, 1, 2],
                [2, 2, 2, 0, 1],
                [2, 2, 2, 2, 2],
                [2, 1, 2, 2, 2],
            ],
            12,
        ),
    ],
)
class TestSolution:
    def test_minimumOperationsToWriteY(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumOperationsToWriteY(
                grid,
            )
            == output
        )
