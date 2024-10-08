import pytest
from q_0629_kInversePairsArray import Solution


@pytest.mark.parametrize("n, k, output", [(3, 0, 1), (3, 1, 2)])
class TestSolution:
    def test_kInversePairs(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.kInversePairs(
                n,
                k,
            )
            == output
        )
