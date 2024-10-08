import pytest
from q_2133_checkIfEveryRowAndColumnContainsAllNumbers import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[1, 2, 3], [3, 1, 2], [2, 3, 1]], True),
        ([[1, 1, 1], [1, 2, 3], [1, 2, 3]], False),
    ],
)
class TestSolution:
    def test_checkValid(self, matrix: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.checkValid(
                matrix,
            )
            == output
        )
