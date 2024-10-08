import pytest
from q_0668_kthSmallestNumberInMultiplicationTable import Solution


@pytest.mark.parametrize("m, n, k, output", [(3, 3, 5, 3), (2, 3, 6, 6)])
class TestSolution:
    def test_findKthNumber(self, m: int, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.findKthNumber(
                m,
                n,
                k,
            )
            == output
        )
