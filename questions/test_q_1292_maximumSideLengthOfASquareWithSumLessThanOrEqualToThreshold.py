import pytest
from q_1292_maximumSideLengthOfASquareWithSumLessThanOrEqualToThreshold import Solution


@pytest.mark.parametrize(
    "mat, threshold, output",
    [
        ([[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4, 2),
        (
            [
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
            ],
            1,
            0,
        ),
    ],
)
class TestSolution:
    def test_maxSideLength(self, mat: List[List[int]], threshold: int, output: int):
        sc = Solution()
        assert (
            sc.maxSideLength(
                mat,
                threshold,
            )
            == output
        )
