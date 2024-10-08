import pytest
from q_1837_sumOfDigitsInBaseK import Solution


@pytest.mark.parametrize("n, k, output", [(34, 6, 9), (10, 10, 1)])
class TestSolution:
    def test_sumBase(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.sumBase(
                n,
                k,
            )
            == output
        )
