import pytest
from q_2392_buildAMatrixWithConditions import Solution


@pytest.mark.parametrize(
    "k, rowConditions, colConditions, output",
    [
        (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]], [[3, 0, 0], [0, 0, 1], [0, 2, 0]]),
        (3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]], []),
    ],
)
class TestSolution:
    def test_buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
        output: List[List[int]],
    ):
        sc = Solution()
        assert (
            sc.buildMatrix(
                k,
                rowConditions,
                colConditions,
            )
            == output
        )
