import pytest
from q_0378_kthSmallestElementInASortedMatrix import Solution


@pytest.mark.parametrize(
    "matrix, k, output",
    [([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13), ([[-5]], 1, -5)],
)
class TestSolution:
    def test_kthSmallest(self, matrix: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.kthSmallest(
                matrix,
                k,
            )
            == output
        )
