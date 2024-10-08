import pytest
from q_0566_reshapeTheMatrix import Solution


@pytest.mark.parametrize(
    "mat, r, c, output",
    [
        ([[1, 2], [3, 4]], 1, 4, [[1, 2, 3, 4]]),
        ([[1, 2], [3, 4]], 2, 4, [[1, 2], [3, 4]]),
    ],
)
class TestSolution:
    def test_matrixReshape(
        self, mat: List[List[int]], r: int, c: int, output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.matrixReshape(
                mat,
                r,
                c,
            )
            == output
        )
