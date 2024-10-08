import pytest
from q_0440_kThSmallestInLexicographicalOrder import Solution


@pytest.mark.parametrize("n, k, output", [(13, 2, 10), (1, 1, 1)])
class TestSolution:
    def test_findKthNumber(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.findKthNumber(
                n,
                k,
            )
            == output
        )
