import pytest
from q_1314_matrixBlockSum import Solution


@pytest.mark.parametrize(
    "mat, k, output",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            1,
            [[12, 21, 16], [27, 45, 33], [24, 39, 28]],
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            2,
            [[45, 45, 45], [45, 45, 45], [45, 45, 45]],
        ),
    ],
)
class TestSolution:
    def test_matrixBlockSum(
        self, mat: List[List[int]], k: int, output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.matrixBlockSum(
                mat,
                k,
            )
            == output
        )
