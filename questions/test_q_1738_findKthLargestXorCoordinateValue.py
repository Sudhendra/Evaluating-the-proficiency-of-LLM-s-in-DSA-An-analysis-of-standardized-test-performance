import pytest
from q_1738_findKthLargestXorCoordinateValue import Solution


@pytest.mark.parametrize(
    "matrix, k, output",
    [([[5, 2], [1, 6]], 1, 7), ([[5, 2], [1, 6]], 2, 5), ([[5, 2], [1, 6]], 3, 4)],
)
class TestSolution:
    def test_kthLargestValue(self, matrix: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.kthLargestValue(
                matrix,
                k,
            )
            == output
        )
