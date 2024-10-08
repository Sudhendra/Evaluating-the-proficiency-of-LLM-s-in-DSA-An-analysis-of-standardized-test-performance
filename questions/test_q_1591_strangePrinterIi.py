import pytest
from q_1591_strangePrinterIi import Solution


@pytest.mark.parametrize(
    "targetGrid, output",
    [
        ([[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]], True),
        ([[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]], True),
        ([[1, 2, 1], [2, 1, 2], [1, 2, 1]], False),
    ],
)
class TestSolution:
    def test_isPrintable(self, targetGrid: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.isPrintable(
                targetGrid,
            )
            == output
        )
