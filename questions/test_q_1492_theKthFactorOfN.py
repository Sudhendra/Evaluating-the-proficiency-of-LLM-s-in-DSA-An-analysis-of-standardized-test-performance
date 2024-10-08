import pytest
from q_1492_theKthFactorOfN import Solution


@pytest.mark.parametrize("n, k, output", [(12, 3, 3), (7, 2, 7), (4, 4, -1)])
class TestSolution:
    def test_kthFactor(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.kthFactor(
                n,
                k,
            )
            == output
        )
