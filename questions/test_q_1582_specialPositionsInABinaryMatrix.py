import pytest
from q_1582_specialPositionsInABinaryMatrix import Solution


@pytest.mark.parametrize(
    "mat, output",
    [([[1, 0, 0], [0, 0, 1], [1, 0, 0]], 1), ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)],
)
class TestSolution:
    def test_numSpecial(self, mat: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numSpecial(
                mat,
            )
            == output
        )
