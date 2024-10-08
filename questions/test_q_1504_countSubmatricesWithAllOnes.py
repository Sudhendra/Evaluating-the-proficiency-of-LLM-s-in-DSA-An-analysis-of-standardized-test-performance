import pytest
from q_1504_countSubmatricesWithAllOnes import Solution


@pytest.mark.parametrize(
    "mat, output",
    [
        ([[1, 0, 1], [1, 1, 0], [1, 1, 0]], 13),
        ([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]], 24),
    ],
)
class TestSolution:
    def test_numSubmat(self, mat: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numSubmat(
                mat,
            )
            == output
        )
