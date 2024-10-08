import pytest
from q_2643_rowWithMaximumOnes import Solution


@pytest.mark.parametrize(
    "mat, output",
    [
        ([[0, 1], [1, 0]], [0, 1]),
        ([[0, 0, 0], [0, 1, 1]], [1, 2]),
        ([[0, 0], [1, 1], [0, 0]], [1, 2]),
    ],
)
class TestSolution:
    def test_rowAndMaximumOnes(self, mat: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.rowAndMaximumOnes(
                mat,
            )
            == output
        )
