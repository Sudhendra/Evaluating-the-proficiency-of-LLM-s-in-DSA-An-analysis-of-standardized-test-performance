import pytest
from q_1886_determineWhetherMatrixCanBeObtainedByRotation import Solution


@pytest.mark.parametrize(
    "mat, target, output",
    [
        ([[0, 1], [1, 0]], [[1, 0], [0, 1]], True),
        ([[0, 1], [1, 1]], [[1, 0], [0, 1]], False),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]], True),
    ],
)
class TestSolution:
    def test_findRotation(
        self, mat: List[List[int]], target: List[List[int]], output: bool
    ):
        sc = Solution()
        assert (
            sc.findRotation(
                mat,
                target,
            )
            == output
        )
