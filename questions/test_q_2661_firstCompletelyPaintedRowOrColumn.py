import pytest
from q_2661_firstCompletelyPaintedRowOrColumn import Solution


@pytest.mark.parametrize(
    "arr, mat, output",
    [
        ([1, 3, 4, 2], [[1, 4], [2, 3]], 2),
        ([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]], 3),
    ],
)
class TestSolution:
    def test_firstCompleteIndex(
        self, arr: List[int], mat: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.firstCompleteIndex(
                arr,
                mat,
            )
            == output
        )
