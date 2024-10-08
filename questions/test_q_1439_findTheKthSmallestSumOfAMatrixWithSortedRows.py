import pytest
from q_1439_findTheKthSmallestSumOfAMatrixWithSortedRows import Solution


@pytest.mark.parametrize(
    "mat, k, output",
    [
        ([[1, 3, 11], [2, 4, 6]], 5, 7),
        ([[1, 3, 11], [2, 4, 6]], 9, 17),
        ([[1, 10, 10], [1, 4, 5], [2, 3, 6]], 7, 9),
    ],
)
class TestSolution:
    def test_kthSmallest(self, mat: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.kthSmallest(
                mat,
                k,
            )
            == output
        )
