import pytest
from q_0793_preimageSizeOfFactorialZeroesFunction import Solution


@pytest.mark.parametrize("k, output", [(0, 5), (5, 0), (3, 5)])
class TestSolution:
    def test_preimageSizeFZF(self, k: int, output: int):
        sc = Solution()
        assert (
            sc.preimageSizeFZF(
                k,
            )
            == output
        )
